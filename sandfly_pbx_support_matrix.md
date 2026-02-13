# 📞 Sandfly Security – PBX / VoIP Compatibility Matrix

Columns:
Vendor | Platform / Product Line | Operating System | Exact Release / Version | Architecture | Support Status | Notes

---

# ✅ SUPPORTED

| Vendor | Platform / Product Line | Operating System | Exact Release / Version | Architecture | Support Status | Notes |
|--------|--------------------------|------------------|--------------------------|-------------|----------------|------|
| 3CX | 3CX Linux Edition | Debian | 10 (Buster) | x86_64 | ✅ Supported | Standard Linux |
| 3CX | 3CX Linux Edition | Debian | 11 (Bullseye) | x86_64 | ✅ Supported | Standard Linux |
| Asterisk | Source Install | Debian | 8 (Jessie) | x86_64 | ✅ Supported | Validate glibc |
| Asterisk | Source Install | Debian | 9 (Stretch) | x86_64 | ✅ Supported | Standard Linux |
| Asterisk | Source Install | Debian | 10 (Buster) | x86_64 | ✅ Supported | Standard Linux |
| Asterisk | Source Install | Debian | 11 (Bullseye) | x86_64 | ✅ Supported | Standard Linux |
| Asterisk | Source Install | CentOS | 6 | x86_64 | ✅ Supported | Kernel validation |
| Asterisk | Source Install | CentOS | 7 | x86_64 | ✅ Supported | Standard Linux |
| Elastix | Linux Build | CentOS | 6 | x86_64 | ✅ Supported | Standard Linux |
| Elastix | Linux Build | CentOS | 7 | x86_64 | ✅ Supported | Standard Linux |
| FreePBX | Distro | Debian | 10 | x86_64 | ✅ Supported | Standard Linux |
| FreePBX | Distro | Debian | 11 | x86_64 | ✅ Supported | Standard Linux |
| FreeSWITCH | Linux Install | Debian | 10 | x86_64 | ✅ Supported | Standard Linux |
| FusionPBX | Linux Install | Ubuntu | 20.04 | x86_64 | ✅ Supported | Standard Linux |
| Issabel | Linux Build | CentOS | 7 | x86_64 | ✅ Supported | Standard Linux |
| Kamailio | Linux Install | Debian | 10 | x86_64 | ✅ Supported | Standard Linux |
| OpenSIPS | Linux Install | Debian | 10 | x86_64 | ✅ Supported | Standard Linux |
| Rocky Linux PBX | Custom Install | Rocky Linux | 8 | x86_64 | ✅ Supported | Standard Linux |
| Sangoma | Asterisk (Non-Appliance) | Debian | 10 | x86_64 | ✅ Supported | Software install |
| SUSE-based PBX | Custom Install | SLES | 12 | x86_64 | ✅ Supported | Standard Linux |
| Ubuntu PBX | Custom Install | Ubuntu | 18.04 | x86_64 | ✅ Supported | Standard Linux |
| Ubuntu PBX | Custom Install | Ubuntu | 20.04 | x86_64 | ✅ Supported | Standard Linux |
| Wazo | Linux Install | Debian | 10 | x86_64 | ✅ Supported | Standard Linux |
| Yate | Linux Install | Debian | 10 | x86_64 | ✅ Supported | Standard Linux |

---

# ⚠️ LIMITED SUPPORT

| Vendor | Platform / Product Line | Operating System | Exact Release / Version | Architecture | Support Status | Notes |
|--------|--------------------------|------------------|--------------------------|-------------|----------------|------|
| Adtran | NetVanta SBC | Embedded Linux | Vendor firmware | Embedded | ⚠️ Limited | Validate access |
| Alcatel-Lucent | OmniPCX Enterprise (Modern) | Embedded Linux | Vendor firmware | x86_64 | ⚠️ Limited | Appliance shell |
| AudioCodes | Mediant SBC | Embedded Linux | Vendor firmware | x86_64 / ARM | ⚠️ Limited | Restricted access |
| Avaya | Aura | RHEL | 6 | x86_64 | ⚠️ Limited | Restricted shell |
| Avaya | Aura | RHEL | 7 | x86_64 | ⚠️ Limited | Restricted shell |
| Avaya | Aura | RHEL | 8 | x86_64 | ⚠️ Limited | sudo required |
| Avaya | IP Office Server Edition | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Appliance build |
| BroadSoft | BroadWorks | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Carrier-managed |
| Cisco | CUCM | CentOS-based VOS | 7 | x86_64 | ⚠️ Limited | Locked-down OS |
| Cisco | CUCM | CentOS-based VOS | 8 | x86_64 | ⚠️ Limited | Locked-down OS |
| Cisco | Unity Connection | CentOS-based VOS | 7 | x86_64 | ⚠️ Limited | Restricted |
| Cisco | IM & Presence | CentOS-based VOS | 7 | x86_64 | ⚠️ Limited | Restricted |
| Dialogic | Media Gateway | Embedded Linux | Vendor firmware | Embedded | ⚠️ Limited | Appliance |
| Ericsson | IMS Core | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Carrier platform |
| Fortinet | FortiVoice | Embedded Linux | Vendor firmware | Embedded | ⚠️ Limited | Appliance |
| Genesys | SIP Server Appliance | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Restricted |
| Grandstream | UCM62xx / UCM63xx | Embedded Linux | Vendor firmware | ARM | ⚠️ Limited | BusyBox |
| Huawei | Softswitch | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Carrier platform |
| Metaswitch | Perimeta SBC | Embedded Linux | Vendor firmware | x86_64 | ⚠️ Limited | Appliance |
| Mitel | MiVoice Business | MSL | 5 | x86_64 | ⚠️ Limited | Schedule scans |
| Mitel | MiVoice Business | MSL | 6 | x86_64 | ⚠️ Limited | Kernel check |
| NEC | Univerge SV9100 | Embedded Linux | Vendor firmware | Embedded | ⚠️ Limited | Restricted shell |
| Nokia | IMS | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Carrier platform |
| Oracle | Acme Packet SBC | Embedded Linux | Vendor firmware | x86_64 | ⚠️ Limited | Appliance |
| Panasonic | KX-NS | Embedded Linux | Vendor firmware | Embedded | ⚠️ Limited | Restricted |
| Ribbon | SBC | Embedded Linux | Vendor firmware | x86_64 | ⚠️ Limited | Validate SSH |
| Sangoma | PBXact Appliance | CentOS | 7 | x86_64 | ⚠️ Limited | Appliance |
| ShoreTel | Connect | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Appliance |
| Unify | OpenScape Voice | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Restricted |
| Yeastar | P-Series | Embedded Linux | Vendor firmware | ARM | ⚠️ Limited | Appliance |
| ZTE | IMS | Linux (Vendor) | Vendor release | x86_64 | ⚠️ Limited | Carrier platform |

---

# ❌ NOT SUPPORTED

| Vendor | Platform / Product Line | Operating System | Exact Release / Version | Architecture | Support Status | Notes |
|--------|--------------------------|------------------|--------------------------|-------------|----------------|------|
| Alcatel | OmniPCX 4200 | Proprietary | All | Proprietary | ❌ Not Supported | Pre-Linux |
| Alcatel | OmniPCX 4400 | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| AT&T | 5ESS | Proprietary RTOS | All | Proprietary | ❌ Not Supported | Class-5 switch |
| Avaya | Communication Manager (Legacy) | Solaris | 8 | SPARC | ❌ Not Supported | Non-Linux |
| Avaya | Communication Manager (Legacy) | Solaris | 9 | SPARC | ❌ Not Supported | Non-Linux |
| Avaya | Definity | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Ericsson | MD110 | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Fujitsu | F9600 | Proprietary | All | Proprietary | ❌ Not Supported | Legacy switch |
| Hitachi | Legacy PBX | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Inter-Tel | Axxess | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Iwatsu | Legacy PBX | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| LG-Ericsson | Legacy PBX | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Lucent | 5ESS | Proprietary RTOS | All | Proprietary | ❌ Not Supported | Telecom switch |
| Lucent | Definity | Oryx | All | Proprietary | ❌ Not Supported | RTOS |
| Mitel | SX-200 | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| NEC | NEAX 2400 | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Nortel | CS1000 | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Nortel | Meridian 1 | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Panasonic | KX-TDA | Proprietary | All | Embedded | ❌ Not Supported | Legacy OS |
| Samsung | OfficeServ (Legacy) | Proprietary | All | Embedded | ❌ Not Supported | Legacy OS |
| Siemens | HiPath 4000 (Legacy) | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Toshiba | Strata CTX | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
| Vertical | Wave (Legacy) | Proprietary | All | Proprietary | ❌ Not Supported | Legacy OS |
