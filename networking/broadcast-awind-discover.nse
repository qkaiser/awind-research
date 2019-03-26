local nmap = require "nmap"
local packet = require "packet"
local stdnse = require "stdnse"
local target = require "target"

description = [[
Discovers Awind wireless presentation devices and derivatives using the same
method as the manufacturers own client applications. An interface needs to be
configured, as the script broadcasts a UDP packet.

The script needs to be run as a privileged user, typically root.

References:
* TODO
]]

---
-- @usage
-- nmap -e eth0 --script broadcast-awind-discover
--
-- @output
-- | broadcast-awind-discover:
-- |   192.168.1.2:
-- |     Hostname: Airmedia1
-- |   192.168.1.3:
-- |_    Hostname: AirMedia2
--
-- @args broadcast-awind-discover.timeout time in seconds to wait for a response
--       (default: 1s)

author = "Quentin Kaiser"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"broadcast", "safe"}


-- preliminary checks
local interface = stdnse.get_script_args(SCRIPT_NAME .. ".interface") or nmap.get_interface()

prerule = function()
  if not nmap.is_privileged() then
    stdnse.verbose1("Not running for lack of privileges.")
    return false
  end

  local has_interface = ( interface ~= nil )
  if ( not(has_interface) ) then
    stdnse.verbose1("No network interface was supplied, aborting.")
    return false
  end
  return true
end

action = function(host, port)
  local sock, co
  sock = nmap.new_socket()

  local timeout = stdnse.parse_timespec(stdnse.get_script_args(SCRIPT_NAME .. ".timeout"))
  timeout = (timeout or 1) * 1000

  -- listen for a response
  sock:set_timeout(timeout)
  sock:pcap_open(interface, 1500, false, "ip && udp && port 1047 && greater 64")
  send_discover()
  local start_time = nmap.clock_ms()
  local results = stdnse.output_table()
  while( nmap.clock_ms() - start_time < timeout ) do
    local status, plen, _, layer3 = sock:pcap_receive()

    if ( status ) then
      local p = packet.Packet:new( layer3, #layer3)

      if ( p and p.udp_dport ) then
        -- parsing the result
        local IP = p.ip_src
        local Hostname = layer3:match("\x0c([^\x00]*)")

        -- add nodes
        if target.ALLOW_NEW_TARGETS then
          target.add(IP)
        end

        local output = stdnse.output_table()
        output['Hostname'] = Hostname
        results[IP] = output
      end
    end
  end
  sock:close()

  if #results > 0 then
    return results
  end
end

function send_discover()
  local host="255.255.255.255"
  local port="1047"
  local socket = nmap.new_socket("udp")

  local status = socket:sendto(host, port, "WPPS")
  if not status then return end
  socket:close()

  return true
end
