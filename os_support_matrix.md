## Supporting Operating Systems

Sandfly supports a broad range of Linux-based operating systems and platforms. 

### Supported Linux Distribution Builds (Kernel ≥ 2.6.32)

---
## Supporting Operating Systems

Sandfly supports **Linux-based operating systems only**.  

Support is determined by **Linux kernel capability (≥ 2.6.32)** and **SSH access**, not by Unix lineage or proprietary UNIX variants.

Traditional UNIX operating systems (AIX, Solaris, HP-UX) are **not supported**.

---

### Supported Linux Distribution Builds  
**Minimum requirement: Linux kernel 2.6.32 or newer**

---

#### Red Hat–based Distributions

| Distribution | Specific Release | Kernel Version | Supported |
|-------------|------------------|---------------|-----------|
| RHEL | 6.0 – 6.10 | 2.6.32 | ✅ |
| RHEL | 7.0 – 7.9 | 3.10 | ✅ |
| RHEL | 8.0 – 8.10 | 4.18 | ✅ |
| RHEL | 9.0 – 9.x | 5.14 | ✅ |
| CentOS | 6.0 – 6.10 | 2.6.32 | ✅ |
| CentOS | 7.0 – 7.9 | 3.10 | ✅ |
| CentOS Stream | 8 | 4.18 | ✅ |
| CentOS Stream | 9 | 5.14 | ✅ |
| AlmaLinux | 8.x | 4.18 | ✅ |
| AlmaLinux | 9.x | 5.14 | ✅ |
| Rocky Linux | 8.x | 4.18 | ✅ |
| Rocky Linux | 9.x | 5.14 | ✅ |

---

#### Debian / Ubuntu–based Distributions

| Distribution | Specific Release | Kernel Version | Supported |
|-------------|------------------|---------------|-----------|
| Debian | 6 (Squeeze) | 2.6.32 | ✅ |
| Debian | 7 (Wheezy) | 3.2 | ✅ |
| Debian | 8 (Jessie) | 3.16 | ✅ |
| Debian | 9 (Stretch) | 4.9 | ✅ |
| Debian | 10 (Buster) | 4.19 | ✅ |
| Debian | 11 (Bullseye) | 5.10 | ✅ |
| Debian | 12 (Bookworm) | 6.1 | ✅ |
| Ubuntu | 10.04 LTS | 2.6.32 | ✅ |
| Ubuntu | 12.04 LTS | 3.2 | ✅ |
| Ubuntu | 14.04 LTS | 3.13 | ✅ |
| Ubuntu | 16.04 LTS | 4.4 | ✅ |
| Ubuntu | 18.04 LTS | 4.15 | ✅ |
| Ubuntu | 20.04 LTS | 5.4 | ✅ |
| Ubuntu | 22.04 LTS | 5.15 | ✅ |
| Ubuntu | 24.04 LTS | 6.8 | ✅ |

---

#### Other Linux Distributions

| Distribution | Specific Release / Condition | Kernel Version | Supported |
|-------------|-----------------------------|---------------|-----------|
| Fedora | 16+ | ≥ 3.x | ✅ |
| SUSE Linux Enterprise | 11 SP1+ | ≥ 2.6.32 | ✅ |
| SUSE Linux Enterprise | 12 | 3.12 | ✅ |
| SUSE Linux Enterprise | 15 | 4.12+ | ✅ |


---
### Supported Linux Distribution Builds  
**Minimum requirement: Linux kernel 2.6.32 or newer**

---

#### Arch Linux

| Distribution | Release / Snapshot | Typical Kernel Version | Supported |
|-------------|--------------------|------------------------|-----------|
| Arch Linux | 2010–2011 snapshots | 2.6.32–2.6.38 | ✅ |
| Arch Linux | 2012–2014 snapshots | 3.x | ✅ |
| Arch Linux | 2015–2018 snapshots | 4.x | ✅ |
| Arch Linux | 2019–2022 snapshots | 5.x | ✅ |
| Arch Linux | 2023–present snapshots | 6.x | ✅ |

---

#### Gentoo Linux

| Distribution | Profile / Era | Typical Kernel Version | Supported |
|-------------|---------------|------------------------|-----------|
| Gentoo | Legacy profiles (2010–2011) | 2.6.32–2.6.39 | ✅ |
| Gentoo | Stable profiles (2012–2015) | 3.x | ✅ |
| Gentoo | Stable profiles (2016–2019) | 4.x | ✅ |
| Gentoo | Stable profiles (2020–2022) | 5.x | ✅ |
| Gentoo | Current stable/testing | 6.x | ✅ |

Support applies regardless of userland profile, USE flags, or package selection, provided the running kernel meets the minimum requirement and SSH access is available.

---

### Cloud & Virtualization Platforms  
**Linux images only — minimum kernel requirement: 2.6.32 or newer**

#### Amazon Web Services (AWS)

| Platform | Image / Release | Kernel Version | Supported |
|---------|-----------------|----------------|-----------|
| Amazon Linux | Amazon Linux 1 | 4.14 | ✅ |
| Amazon Linux | Amazon Linux 2 | 4.14 / 5.10 | ✅ |
| Amazon Linux | Amazon Linux 2023 | 6.1 | ✅ |
| AWS | Custom Linux AMIs | ≥ 2.6.32 | ✅ |

---

#### DigitalOcean

| Platform | Image Type | Kernel Version | Supported |
|---------|------------|----------------|-----------|
| DigitalOcean | Ubuntu images | 3.x–6.x | ✅ |
| DigitalOcean | Debian images | 3.x–6.x | ✅ |
| DigitalOcean | Fedora images | 3.x–6.x | ✅ |
| DigitalOcean | Custom droplets | ≥ 2.6.32 | ✅ |

---

#### Microsoft Azure

| Platform | Image Type | Kernel Version | Supported |
|---------|------------|----------------|-----------|
| Azure | Ubuntu marketplace images | 3.x–6.x | ✅ |
| Azure | RHEL marketplace images | 3.x–5.x | ✅ |
| Azure | Debian marketplace images | 3.x–6.x | ✅ |
| Azure | Custom Linux images | ≥ 2.6.32 | ✅ |


---

### Network & Embedded Devices

### Cisco Network Operating System Support Matrix (Kernel-Based)

Support is determined by whether the platform runs a Linux-based OS meeting the minimum kernel requirement (≥ 2.6.32).

---

## Cisco Nexus NX-OS

### Supported NX-OS Platforms

| NX-OS Release Train | Linux Kernel Basis | Supported Nexus Families | Supported |
|--------------------|-------------------|--------------------------|-----------|
| 9.3(x) | Linux 3.10 | Nexus 3000, Nexus 9000 | ✅ |
| 10.2(x) | Linux 3.10 | Nexus 9000 | ✅ |
| 10.3(x) | Linux 3.10 | Nexus 9000 | ✅ |
| 10.4(x) | Linux 3.10 | Nexus 9000 | ✅ |
| 10.5(x) | Linux 3.10 | Nexus 3500, Nexus 3600, Nexus 9000 | ✅ |
| 10.6(x) | Linux 3.10 | Nexus 9000 | ✅ |

### Not Supported NX-OS Platforms

| NX-OS Release Train | Linux Kernel Basis | Nexus Families | Supported | Reason |
|--------------------|-------------------|----------------|-----------|--------|
| 4.x | Linux 2.6 | Early Nexus platforms | ❌ | Kernel below minimum |
| 5.x | Linux 2.6 | Early Nexus platforms | ❌ | Kernel below minimum |
| 6.x | Linux 2.6 | Early Nexus platforms | ❌ | Kernel below minimum |
| 7.x (early) | Linux 2.6 | Early Nexus platforms | ❌ | Kernel below minimum |

---

## Cisco IOS XR

### Supported IOS XR Platforms

| IOS XR Release | Linux Kernel Basis | Supported Hardware Families | Supported |
|---------------|-------------------|-----------------------------|-----------|
| IOS XR 6.x+ | Linux-based | ASR 9000 Series | ✅ |
| IOS XR 6.x+ | Linux-based | NCS 500 Series | ✅ |
| IOS XR 6.x+ | Linux-based | NCS 540 / 5500 Series | ✅ |
| IOS XR 6.x+ | Linux-based | NCS 560 / 6000 Series | ✅ |
| IOS XR 6.x+ | Linux-based | 8000 Series Routers | ✅ |

### Not Supported IOS XR Platforms

| IOS XR Release | Hardware Families | Supported | Reason |
|---------------|-------------------|-----------|--------|
| IOS XR pre-6.x | Legacy CRS / XR platforms | ❌ | Non-Linux or kernel below minimum |

---

## Support Rule Summary

- NX-OS **9.x and 10.x** → Linux 3.10 → **Supported**
- IOS XR **6.x and newer** → Linux-based → **Supported**
- Any Cisco network OS based on **Linux kernel < 2.6.32** → **Not Supported**

---

---
### Juniper Network Device Support (Linux-Based Operating Systems)

Support applies to **Linux-based Juniper operating systems** that meet the minimum kernel requirement (≥ 2.6.32) and provide SSH access.

---

#### Juniper Junos OS (Traditional → Linux-Based Transition)

| Operating System | Release / Era | Linux Kernel Basis | Supported |
|------------------|---------------|--------------------|-----------|
| Junos OS | Pre-15.x (FreeBSD-based) | Non-Linux | ❌ |
| Junos OS | 15.x (early transition) | Hybrid / partial Linux | ❌ |
| Junos OS | 17.x – 18.x | Linux-based | ✅ |
| Junos OS | 19.x – 20.x | Linux-based | ✅ |
| Junos OS | 21.x – 22.x | Linux-based | ✅ |
| Junos OS | 23.x – present | Linux-based | ✅ |

Support applies to Junos OS releases after Juniper’s transition to a Linux-based architecture.

---

#### Juniper Evolved OS (Junos EVO)

| Operating System | Release Train | Linux Kernel Basis | Supported |
|------------------|---------------|--------------------|-----------|
| Junos Evolved OS (EVO) | All releases | Linux-based | ✅ |

Junos Evolved OS is natively Linux-based and designed for modern routing and switching platforms.

---

#### Juniper Hardware Families (Linux-Based OS)

| Hardware Family | Operating System | Supported |
|-----------------|------------------|-----------|
| MX Series Routers | Junos OS (Linux-based releases) | ✅ |
| PTX Series Routers | Junos OS / Junos EVO | ✅ |
| QFX Series Switches | Junos OS (Linux-based releases) | ✅ |
| EX Series Switches | Junos OS (Linux-based releases) | ✅ |

---

**Notes**
- Traditional FreeBSD-based Junos OS releases are **not supported**
- Support is determined by **Linux-based OS architecture**, not hardware alone
- SSH access is required

---
### Embedded Linux System Support

Support applies to **embedded and appliance-based Linux systems** that meet the minimum kernel requirement (≥ 2.6.32) and provide SSH access.

---

#### Embedded Linux Platforms (General)

| Platform Type | Release / Era | Typical Kernel Version | Supported |
|--------------|---------------|------------------------|-----------|
| Embedded Linux | Legacy embedded systems (2010–2011) | 2.6.32–2.6.39 | ✅ |
| Embedded Linux | Mid-generation embedded systems (2012–2015) | 3.x | ✅ |
| Embedded Linux | Modern embedded systems (2016–2019) | 4.x | ✅ |
| Embedded Linux | Current embedded systems (2020–present) | 5.x–6.x | ✅ |

Support applies regardless of vendor distribution (Yocto, Buildroot, custom BSPs), provided the running kernel meets the minimum requirement.

---

#### Raspberry Pi Platforms

| Platform | OS / Release Era | Typical Kernel Version | Supported |
|---------|------------------|------------------------|-----------|
| Raspberry Pi | Early Raspbian (2012–2014) | 3.x | ✅ |
| Raspberry Pi | Raspbian / Raspberry Pi OS (2015–2018) | 4.x | ✅ |
| Raspberry Pi | Raspberry Pi OS (2019–2022) | 5.x | ✅ |
| Raspberry Pi | Raspberry Pi OS (2023–present) | 6.x | ✅ |

---

#### Embedded CPU Architectures

| Architecture | Kernel Requirement | Supported |
|-------------|--------------------|-----------|
| ARM | Kernel ≥ 2.6.32 (newer required on some platforms) | ✅ |
| ARM64 (AArch64) | Kernel ≥ 3.x | ✅ |
| MIPS | Kernel ≥ 2.6.32 (platform-dependent) | ✅ |
| PowerPC / IBM Power | Kernel ≥ 3.x | ✅ |

---
