# Awind Research

This repository holds interesting bits and pieces related to research I performed on wireless presentation devices manufactured by Awindinc and OEM'ed to multiple manufacturers.

The repository is split into these subsections:

* **hardware** - hardware hacking stuff, mostly for MMC dumping and pinout documentation
* **networking** - PIN code bruteforcer, custom Nmap scripts and fingerprints
* **exploits** - Metasploit modules and Python-based exploits.


## Affected devices

The following devices were OEM'ed by Awind and are therefore affected by the same issues.

* [Crestron Airmedia AM-100](https://www.crestron.com/en-US/Products/Workspace-Solutions/Wireless-Presentation-Solutions/AirMedia-Presentation-Gateways/AM-100)
* [Crestron Airmedia AM-101](https://www.crestron.com/Products/Workspace-Solutions/Wireless-Presentation-Solutions/AirMedia-Presentation-Gateways/AM-101)
* [Awind wePresent WiPG-1000](http://www.awindinc.com/products_wepresent_wipg_1000.html)
* [Awind wePresent WiPG-1500](http://www.awindinc.com/products_wepresent_wipg_1500.html)
* [Awind wePresent WiPG-2000](http://www.awindinc.com/products_wepresent_wipg_2000.html)
* [Barco WiPG-1000](https://www.barco.com/en/product/wepresent-wipg-1000)
* [Barco WiPG-1600w](https://www.barco.com/en/product/wepresent-wipg-1600w)
* [Barco WiCS-2100](https://www.barco.com/en/product/wepresent-wics-2100)
* [Newline Trucast 1](#)
* [Newline Trucast 2](https://newlineinteractive.freshdesk.com/support/solutions/articles/8000022611-trucast-2-twp-1500-)
* [Newline Trucast 3](https://www.touchboards.com/newline-epr5a31820-000/)
* [InFocus Liteshow 1](#)
* [InFocus Liteshow 2](https://www.infocus.com/products/inliteshow2)
* [InFocus Liteshow 3](https://www.infocus.com/products/inliteshow3)
* [InFocus Liteshow 4](https://www.infocus.com/products/inliteshow4)
* [Black Box Network Services WPS](#)
* [Black Box Network Services WPS-Interactive](#)
* [Black Box Network Services WPS-IPro2](#)
* [Extron ShareLink 200](https://www.extron.com/company/article.aspx?id=sharelink200nspr)
* [Extron ShareLink 250 W](https://www.extron.com/article/sharelink200ad)
* [Haworth WPS](https://la.haworth.com/)
* [Teqavit WiPS710-ENT](http://www.teqavit.com/wips710-ent)
* [Teqavit WiPS710-EDU](http://www.teqavit.com/wips710-edu)
* [Teqavit WiPS710-NET](http://www.teqavit.com/wips710-net)
* [Teqavit WiD510-EDU](http://www.teqavit.com/wid510-edu)
* [Teqavit WiD510-ENT](http://www.teqavit.com/wid510-ent)
* [Teqavit WiD510-NET](http://www.teqavit.com/wid510-net)

This list is non-exhaustive as it is based on devices observed on the public Internet. If you are aware of other brand/model, just shoot me an email.

#### Known Default Creds

Default credentials exported from installation manuals.

| Manufacturer | Username | Password |
| --------------- | --------- | ------- |
| Airmedia | admin | admin |
| Extron | admin | configure |
| Teqavit | admin | Admin&11 |
| Infocus | admin | admin |
| Barco | admin | admin |
| Newline | admin | admin |



## References

* [Man-in-the-conference-room - Part I (Intro)](https://qkaiser.github.io/pentesting/2019/03/25/awind-device/)
* [Man-in-the-conference-room - Part II (Hardware Hacking)](https://qkaiser.github.io/pentesting/2019/03/25/awind-device-hardware/)
* [Man-in-the-conference-room - Part III (Network Assessment)](https://qkaiser.github.io/pentesting/2019/03/26/awind-device-network/)
* [Man-in-the-conference-room - Part IV (Vulnerability Research & Development)](https://qkaiser.github.io/pentesting/2019/03/27/awind-device-vrd/)
* [Man-in-the-conference-room - Part V (Huntin OEMs)](https://qkaiser.github.io/pentesting/2019/03/28/awind-device-oemhunt/)
* [Man-in-the-conference-room - Part VI (Conclusion)](https://qkaiser.github.io/pentesting/2019/04/23/awind-device-conclusion/)
