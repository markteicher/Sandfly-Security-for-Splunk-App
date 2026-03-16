![Sandfly Security](docs/images/sandfly_logo.jpg)

# Sandfly Security for Splunk App

## Overview

Sandfly Security is an agentless intrusion detection and incident response platform for Linux. 

Sandfly Security automatically analyzes Linux hosts for intruders 24 hours a day without loading any software on endpoints. 

Sandfly Security retrieves security, hardware, operating system, and related system data from Linux hosts and makes this data available for analysis. Sandfly operates across virtually all Linux distributions immediately and is designed to function without introducing risk to system stability or performance.

The Sandfly Security for Splunk App is a single Splunk application that ingests events from a Sandfly Security server using the Sandfly Security REST API. The app ingests data into a user-specified Splunk index and assigns the correct sourcetype to each event. All events are ingested in JSON format to preserve the original structure and content of the Sandfly data.

The Splunk app provides dashboards, reports, and search logic for analyzing data ingested from a Sandfly Security server. 

This includes Sandfly Security alarms, suspicious activity results, SSH Hunter data, host inventory, and Sandfly server audit and error logs. 

Data retrieved by Sandfly Security can also be used by Splunk users to build searches, reports, anomaly detection models, and incident response workflows within Splunk.

The Splunk App is intended to surface Sandfly data directly inside Splunk so that Asset Owners and operational teams can view, analyze and action Sandfly Security results without requiring access to the Sandfly Security user interface.

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-yellow.svg)



---
⚠️ Disclaimer

These tools are not official Sandfly Security products or utilities

Use of this software is not covered by any license, warranty, or support agreement you may have with Sandfly
Security.

---
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

| Distribution     | Specific Release | Kernel Version | Supported |
|-----------------|-----------------|----------------|-----------|
| RHEL            | 6.0             | 2.6.32         | ✅        |
| RHEL            | 6.1             | 2.6.32         | ✅        |
| RHEL            | 6.2             | 2.6.32         | ✅        |
| RHEL            | 6.3             | 2.6.32         | ✅        |
| RHEL            | 6.4             | 2.6.32         | ✅        |
| RHEL            | 6.5             | 2.6.32         | ✅        |
| RHEL            | 6.6             | 2.6.32         | ✅        |
| RHEL            | 6.7             | 2.6.32         | ✅        |
| RHEL            | 6.8             | 2.6.32         | ✅        |
| RHEL            | 6.9             | 2.6.32         | ✅        |
| RHEL            | 6.10            | 2.6.32         | ✅        |
| RHEL            | 7.0             | 3.10           | ✅        |
| RHEL            | 7.1             | 3.10           | ✅        |
| RHEL            | 7.2             | 3.10           | ✅        |
| RHEL            | 7.3             | 3.10           | ✅        |
| RHEL            | 7.4             | 3.10           | ✅        |
| RHEL            | 7.5             | 3.10           | ✅        |
| RHEL            | 7.6             | 3.10           | ✅        |
| RHEL            | 7.7             | 3.10           | ✅        |
| RHEL            | 7.8             | 3.10           | ✅        |
| RHEL            | 7.9             | 3.10           | ✅        |
| RHEL            | 8.0             | 4.18           | ✅        |
| RHEL            | 8.1             | 4.18           | ✅        |
| RHEL            | 8.2             | 4.18           | ✅        |
| RHEL            | 8.3             | 4.18           | ✅        |
| RHEL            | 8.4             | 4.18           | ✅        |
| RHEL            | 8.5             | 4.18           | ✅        |
| RHEL            | 8.6             | 4.18           | ✅        |
| RHEL            | 8.7             | 4.18           | ✅        |
| RHEL            | 8.8             | 4.18           | ✅        |
| RHEL            | 8.9             | 4.18           | ✅        |
| RHEL            | 8.10            | 4.18           | ✅        |
| RHEL            | 9.0             | 5.14           | ✅        |
| RHEL            | 9.1             | 5.14           | ✅        |
| RHEL            | 9.2             | 5.14           | ✅        |
| RHEL            | 9.3             | 5.14           | ✅        |
| RHEL            | 9.4             | 5.14           | ✅        |
| RHEL            | 9.5             | 5.14           | ✅        |
| RHEL            | 9.6             | 5.14           | ✅        |
| CentOS          | 6.0             | 2.6.32         | ✅        |
| CentOS          | 6.1             | 2.6.32         | ✅        |
| CentOS          | 6.2             | 2.6.32         | ✅        |
| CentOS          | 6.3             | 2.6.32         | ✅        |
| CentOS          | 6.4             | 2.6.32         | ✅        |
| CentOS          | 6.5             | 2.6.32         | ✅        |
| CentOS          | 6.6             | 2.6.32         | ✅        |
| CentOS          | 6.7             | 2.6.32         | ✅        |
| CentOS          | 6.8             | 2.6.32         | ✅        |
| CentOS          | 6.9             | 2.6.32         | ✅        |
| CentOS          | 6.10            | 2.6.32         | ✅        |
| CentOS          | 7.0             | 3.10           | ✅        |
| CentOS          | 7.1             | 3.10           | ✅        |
| CentOS          | 7.2             | 3.10           | ✅        |
| CentOS          | 7.3             | 3.10           | ✅        |
| CentOS          | 7.4             | 3.10           | ✅        |
| CentOS          | 7.5             | 3.10           | ✅        |
| CentOS          | 7.6             | 3.10           | ✅        |
| CentOS          | 7.7             | 3.10           | ✅        |
| CentOS          | 7.8             | 3.10           | ✅        |
| CentOS          | 7.9             | 3.10           | ✅        |
| CentOS Stream   | 8.0             | 4.18           | ✅        |
| CentOS Stream   | 8.1             | 4.18           | ✅        |
| CentOS Stream   | 8.2             | 4.18           | ✅        |
| CentOS Stream   | 8.3             | 4.18           | ✅        |
| CentOS Stream   | 8.4             | 4.18           | ✅        |
| CentOS Stream   | 8.5             | 4.18           | ✅        |
| CentOS Stream   | 8.6             | 4.18           | ✅        |
| CentOS Stream   | 8.7             | 4.18           | ✅        |
| CentOS Stream   | 8.8             | 4.18           | ✅        |
| CentOS Stream   | 8.9             | 4.18           | ✅        |
| CentOS Stream   | 8.10            | 4.18           | ✅        |
| CentOS Stream   | 9.0             | 5.14           | ✅        |
| CentOS Stream   | 9.1             | 5.14           | ✅        |
| CentOS Stream   | 9.2             | 5.14           | ✅        |
| CentOS Stream   | 9.3             | 5.14           | ✅        |
| CentOS Stream   | 9.4             | 5.14           | ✅        |
| CentOS Stream   | 9.5             | 5.14           | ✅        |
| CentOS Stream   | 9.6             | 5.14           | ✅        |
| AlmaLinux       | 8.0             | 4.18           | ✅        |
| AlmaLinux       | 8.1             | 4.18           | ✅        |
| AlmaLinux       | 8.2             | 4.18           | ✅        |
| AlmaLinux       | 8.3             | 4.18           | ✅        |
| AlmaLinux       | 8.4             | 4.18           | ✅        |
| AlmaLinux       | 8.5             | 4.18           | ✅        |
| AlmaLinux       | 8.6             | 4.18           | ✅        |
| AlmaLinux       | 8.7             | 4.18           | ✅        |
| AlmaLinux       | 8.8             | 4.18           | ✅        |
| AlmaLinux       | 8.9             | 4.18           | ✅        |
| AlmaLinux       | 8.10            | 4.18           | ✅        |
| AlmaLinux       | 9.0             | 5.14           | ✅        |
| AlmaLinux       | 9.1             | 5.14           | ✅        |
| AlmaLinux       | 9.2             | 5.14           | ✅        |
| AlmaLinux       | 9.3             | 5.14           | ✅        |
| AlmaLinux       | 9.4             | 5.14           | ✅        |
| AlmaLinux       | 9.5             | 5.14           | ✅        |
| AlmaLinux       | 9.6             | 5.14           | ✅        |
| Rocky Linux     | 8.0             | 4.18           | ✅        |
| Rocky Linux     | 8.1             | 4.18           | ✅        |
| Rocky Linux     | 8.2             | 4.18           | ✅        |
| Rocky Linux     | 8.3             | 4.18           | ✅        |
| Rocky Linux     | 8.4             | 4.18           | ✅        |
| Rocky Linux     | 8.5             | 4.18           | ✅        |
| Rocky Linux     | 8.6             | 4.18           | ✅        |
| Rocky Linux     | 8.7             | 4.18           | ✅        |
| Rocky Linux     | 8.8             | 4.18           | ✅        |
| Rocky Linux     | 8.9             | 4.18           | ✅        |
| Rocky Linux     | 8.10            | 4.18           | ✅        |
| Rocky Linux     | 9.0             | 5.14           | ✅        |
| Rocky Linux     | 9.1             | 5.14           | ✅        |
| Rocky Linux     | 9.2             | 5.14           | ✅        |
| Rocky Linux     | 9.3             | 5.14           | ✅        |
| Rocky Linux     | 9.4             | 5.14           | ✅        |
| Rocky Linux     | 9.5             | 5.14           | ✅        |
| Rocky Linux     | 9.6             | 5.14           | ✅        |

---

## Debian / Ubuntu–based Distributions


| Distribution | Specific Release | Kernel Version | Supported |
|-------------|-----------------|---------------|-----------|
| Debian      | 6 (Squeeze)     | 2.6.32        | ✅        |
| Debian      | 7 (Wheezy)      | 3.2           | ✅        |
| Debian      | 8 (Jessie)      | 3.16          | ✅        |
| Debian      | 9 (Stretch)     | 4.9           | ✅        |
| Debian      | 10 (Buster)     | 4.19          | ✅        |
| Debian      | 11 (Bullseye)   | 5.10          | ✅        |
| Debian      | 12 (Bookworm)   | 6.1           | ✅        |
| Ubuntu      | 10.04 LTS       | 2.6.32        | ✅        |
| Ubuntu      | 12.04 LTS       | 3.2           | ✅        |
| Ubuntu      | 14.04 LTS       | 3.13          | ✅        |
| Ubuntu      | 16.04 LTS       | 4.4           | ✅        |
| Ubuntu      | 18.04 LTS       | 4.15          | ✅        |
| Ubuntu      | 20.04 LTS       | 5.4           | ✅        |
| Ubuntu      | 22.04 LTS       | 5.15          | ✅        |
| Ubuntu      | 24.04 LTS       | 6.8           | ✅        |
---


#### Other Linux Distributions

| Distribution             | Specific Release / Condition | Kernel Version | Supported |
|--------------------------|----------------------------|---------------|-----------|
| Fedora                   | 16                        | 3.1           | ✅        |
| Fedora                   | 17                        | 3.3           | ✅        |
| Fedora                   | 18                        | 3.6           | ✅        |
| Fedora                   | 19                        | 3.8           | ✅        |
| Fedora                   | 20                        | 3.10          | ✅        |
| Fedora                   | 21                        | 3.17          | ✅        |
| Fedora                   | 22                        | 4.0           | ✅        |
| Fedora                   | 23                        | 4.2           | ✅        |
| Fedora                   | 24                        | 4.5           | ✅        |
| Fedora                   | 25                        | 4.6           | ✅        |
| Fedora                   | 26                        | 4.10          | ✅        |
| Fedora                   | 27                        | 4.13          | ✅        |
| Fedora                   | 28                        | 4.16          | ✅        |
| Fedora                   | 29                        | 4.18          | ✅        |
| Fedora                   | 30                        | 5.0           | ✅        |
| Fedora                   | 31                        | 5.3           | ✅        |
| Fedora                   | 32                        | 5.6           | ✅        |
| Fedora                   | 33                        | 5.8           | ✅        |
| Fedora                   | 34                        | 5.11          | ✅        |
| Fedora                   | 35                        | 5.14          | ✅        |
| Fedora                   | 36                        | 5.16          | ✅        |
| Fedora                   | 37                        | 5.17          | ✅        |
| Fedora                   | 38                        | 6.0           | ✅        |
| SUSE Linux Enterprise    | 11 SP1                     | 2.6.32        | ✅        |
| SUSE Linux Enterprise    | 11 SP2                     | 2.6.33        | ✅        |
| SUSE Linux Enterprise    | 11 SP3                     | 2.6.34        | ✅        |
| SUSE Linux Enterprise    | 12                         | 3.12          | ✅        |
| SUSE Linux Enterprise    | 12 SP1                     | 3.16          | ✅        |
| SUSE Linux Enterprise    | 12 SP2                     | 4.4           | ✅        |
| SUSE Linux Enterprise    | 12 SP3                     | 4.12          | ✅        |
| SUSE Linux Enterprise    | 15                         | 4.12+         | ✅        |
| SUSE Linux Enterprise    | 15 SP1                     | 5.3           | ✅        |
| SUSE Linux Enterprise    | 15 SP2                     | 5.4           | ✅        |
| SUSE Linux Enterprise    | 15 SP3                     | 5.6           | ✅        |
| SUSE Linux Enterprise    | 15 SP4                     | 5.14          | ✅        |


---
### Supported Linux Distribution Builds  
**Minimum requirement: Linux kernel 2.6.32 or newer**

---

#### Arch Linux

| Distribution | Release / Snapshot       | Typical Kernel Version | Supported |
|-------------|-------------------------|----------------------|-----------|
| Arch Linux  | 2010 snapshot           | 2.6.32               | ✅        |
| Arch Linux  | 2011 snapshot           | 2.6.38               | ✅        |
| Arch Linux  | 2012 snapshot           | 3.2                  | ✅        |
| Arch Linux  | 2013 snapshot           | 3.5                  | ✅        |
| Arch Linux  | 2014 snapshot           | 3.10                 | ✅        |
| Arch Linux  | 2015 snapshot           | 4.0                  | ✅        |
| Arch Linux  | 2016 snapshot           | 4.2                  | ✅        |
| Arch Linux  | 2017 snapshot           | 4.9                  | ✅        |
| Arch Linux  | 2018 snapshot           | 4.18                 | ✅        |
| Arch Linux  | 2019 snapshot           | 5.0                  | ✅        |
| Arch Linux  | 2020 snapshot           | 5.4                  | ✅        |
| Arch Linux  | 2021 snapshot           | 5.10                 | ✅        |
| Arch Linux  | 2022 snapshot           | 5.15                 | ✅        |
| Arch Linux  | 2023 snapshot           | 6.0                  | ✅        |
| Arch Linux  | 2024 snapshot           | 6.8                  | ✅        |


---


#### Gentoo Linux

| Distribution | Profile / Era | Typical Kernel Version | Supported |
|-------------|-------------------------------|----------------------|-----------|
| Gentoo | Legacy profiles (2010) | 2.6.32 | ✅ |
| Gentoo | Legacy profiles (2011) | 2.6.39 | ✅ |
| Gentoo | Stable profiles (2012) | 3.2 | ✅ |
| Gentoo | Stable profiles (2013) | 3.5 | ✅ |
| Gentoo | Stable profiles (2014) | 3.10 | ✅ |
| Gentoo | Stable profiles (2015) | 3.18 | ✅ |
| Gentoo | Stable profiles (2016) | 4.0 | ✅ |
| Gentoo | Stable profiles (2017) | 4.9 | ✅ |
| Gentoo | Stable profiles (2018) | 4.19 | ✅ |
| Gentoo | Stable profiles (2019) | 4.20 | ✅ |
| Gentoo | Stable profiles (2020) | 5.4 | ✅ |
| Gentoo | Stable profiles (2021) | 5.10 | ✅ |
| Gentoo | Stable profiles (2022) | 5.15 | ✅ |
| Gentoo | Current stable/testing (2023) | 6.0 | ✅ |
| Gentoo | Current stable/testing (2024) | 6.8 | ✅ |


Support applies regardless of userland profile, USE flags, or package selection, provided the running kernel meets the minimum requirement and SSH access is available.

---

### Cloud & Virtualization Platforms  
**Linux images only — minimum kernel requirement: 2.6.32 or newer**

#### Amazon Web Services (AWS)

| Platform | Image / Release | Kernel Version | Supported |
|---------------|---------------------|----------------|-----------|
| Amazon Linux | Amazon Linux 1 | 4.14 | ✅ |
| Amazon Linux | Amazon Linux 2 | 4.14 | ✅ |
| Amazon Linux | Amazon Linux 2 | 5.10 | ✅ |
| Amazon Linux | Amazon Linux 2023 | 6.1 | ✅ |
| AWS | Custom Linux AMIs | ≥ 2.6.32 | ✅ |

---

#### DigitalOcean


| Platform | Image Type | Kernel Version | Supported |
|-------------|----------------|----------------|-----------|
| DigitalOcean | Ubuntu images | 3.0 | ✅ |
| DigitalOcean | Ubuntu images | 3.1 | ✅ |
| DigitalOcean | Ubuntu images | 3.2 | ✅ |
| DigitalOcean | Ubuntu images | 3.3 | ✅ |
| DigitalOcean | Ubuntu images | 3.4 | ✅ |
| DigitalOcean | Ubuntu images | 3.5 | ✅ |
| DigitalOcean | Ubuntu images | 3.6 | ✅ |
| DigitalOcean | Ubuntu images | 3.7 | ✅ |
| DigitalOcean | Ubuntu images | 3.8 | ✅ |
| DigitalOcean | Ubuntu images | 3.9 | ✅ |
| DigitalOcean | Ubuntu images | 4.0 | ✅ |
| DigitalOcean | Ubuntu images | 4.1 | ✅ |
| DigitalOcean | Ubuntu images | 4.2 | ✅ |
| DigitalOcean | Ubuntu images | 4.3 | ✅ |
| DigitalOcean | Ubuntu images | 4.4 | ✅ |
| DigitalOcean | Ubuntu images | 5.0 | ✅ |
| DigitalOcean | Ubuntu images | 5.1 | ✅ |
| DigitalOcean | Ubuntu images | 5.2 | ✅ |
| DigitalOcean | Ubuntu images | 5.3 | ✅ |
| DigitalOcean | Ubuntu images | 5.4 | ✅ |
| DigitalOcean | Ubuntu images | 6.0 | ✅ |
| DigitalOcean | Ubuntu images | 6.1 | ✅ |
| DigitalOcean | Ubuntu images | 6.2 | ✅ |
| DigitalOcean | Ubuntu images | 6.3 | ✅ |
| DigitalOcean | Debian images | 3.0 | ✅ |
| DigitalOcean | Debian images | 3.1 | ✅ |
| DigitalOcean | Debian images | 3.2 | ✅ |
| DigitalOcean | Debian images | 3.3 | ✅ |
| DigitalOcean | Debian images | 3.4 | ✅ |
| DigitalOcean | Debian images | 3.5 | ✅ |
| DigitalOcean | Debian images | 3.6 | ✅ |
| DigitalOcean | Debian images | 3.7 | ✅ |
| DigitalOcean | Debian images | 3.8 | ✅ |
| DigitalOcean | Debian images | 3.9 | ✅ |
| DigitalOcean | Debian images | 4.0 | ✅ |
| DigitalOcean | Debian images | 4.1 | ✅ |
| DigitalOcean | Debian images | 4.2 | ✅ |
| DigitalOcean | Debian images | 4.3 | ✅ |
| DigitalOcean | Debian images | 4.4 | ✅ |
| DigitalOcean | Debian images | 5.0 | ✅ |
| DigitalOcean | Debian images | 5.1 | ✅ |
| DigitalOcean | Debian images | 5.2 | ✅ |
| DigitalOcean | Debian images | 5.3 | ✅ |
| DigitalOcean | Debian images | 5.4 | ✅ |
| DigitalOcean | Debian images | 6.0 | ✅ |
| DigitalOcean | Debian images | 6.1 | ✅ |
| DigitalOcean | Fedora images | 3.0 | ✅ |
| DigitalOcean | Fedora images | 3.1 | ✅ |
| DigitalOcean | Fedora images | 3.2 | ✅ |
| DigitalOcean | Fedora images | 3.3 | ✅ |
| DigitalOcean | Fedora images | 3.4 | ✅ |
| DigitalOcean | Fedora images | 4.0 | ✅ |
| DigitalOcean | Fedora images | 4.1 | ✅ |
| DigitalOcean | Fedora images | 4.2 | ✅ |
| DigitalOcean | Fedora images | 4.3 | ✅ |
| DigitalOcean | Fedora images | 5.0 | ✅ |
| DigitalOcean | Fedora images | 5.1 | ✅ |
| DigitalOcean | Fedora images | 5.2 | ✅ |
| DigitalOcean | Fedora images | 5.3 | ✅ |
| DigitalOcean | Fedora images | 6.0 | ✅ |
| DigitalOcean | Fedora images | 6.1 | ✅ |
| DigitalOcean | Fedora images | 6.2 | ✅ |
| DigitalOcean | Fedora images | 6.3 | ✅ |
| DigitalOcean | Custom droplets | ≥ 2.6.32 | ✅ |

---

#### Microsoft Azure

| Platform | Image Type | Kernel Version | Supported |
|----------|--------------------------|----------------|-----------|
| Azure | Ubuntu marketplace images | 3.x | ✅ |
| Azure | Ubuntu marketplace images | 4.x | ✅ |
| Azure | Ubuntu marketplace images | 5.x | ✅ |
| Azure | Ubuntu marketplace images | 6.x | ✅ |
| Azure | RHEL marketplace images | 3.x | ✅ |
| Azure | RHEL marketplace images | 4.x | ✅ |
| Azure | RHEL marketplace images | 5.x | ✅ |
| Azure | Debian marketplace images | 3.x | ✅ |
| Azure | Debian marketplace images | 4.x | ✅ |
| Azure | Debian marketplace images | 5.x | ✅ |
| Azure | Debian marketplace images | 6.x | ✅ |
| Azure | Custom Linux images | ≥ 2.6.32 | ✅ |


---

### Network & Embedded Devices

### Cisco Network Operating System Support Matrix (Kernel-Based)

Support is determined by whether the platform runs a Linux-based OS meeting the minimum kernel requirement (≥ 2.6.32).

---

## Cisco Nexus NX-OS

### Supported NX-OS Platforms

| Vendor | Platform | Model | NX-OS Release | Linux Kernel Basis | Supported |
|--------|---------|---------|---------------|------------------|-----------|
| Cisco | Nexus | 3000 | 9.3 | Linux 3.10 | ✅ |
| Cisco | Nexus | 9000 | 9.3 | Linux 3.10 | ✅ |
| Cisco | Nexus | 9000 | 10.2 | Linux 3.10 | ✅ |
| Cisco | Nexus | 9000 | 10.3 | Linux 3.10 | ✅ |
| Cisco | Nexus | 9000 | 10.4 | Linux 3.10 | ✅ |
| Cisco | Nexus | 3500 | 10.5 | Linux 3.10 | ✅ |
| Cisco | Nexus | 3600 | 10.5 | Linux 3.10 | ✅ |
| Cisco | Nexus | 9000 | 10.5 | Linux 3.10 | ✅ |
| Cisco | Nexus | 9000 | 10.6 | Linux 3.10 | ✅ |

### Not Supported NX-OS Platforms

| Vendor | Platform | Model / Series | Version / Release | Supported | Reason |
|--------|---------|----------------|-----------------|-----------|--------|
| Cisco | NX-OS | Nexus 1000 | 4.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 1000 | 4.1 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 1000 | 4.2 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 2000 | 4.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 2000 | 4.1 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 2000 | 4.2 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 3000 | 4.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 3000 | 5.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 3000 | 6.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 5000 | 4.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 5000 | 5.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 5000 | 6.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 6000 | 4.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 6000 | 5.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 6000 | 6.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 7000 | 4.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 7000 | 5.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 7000 | 6.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 9000 | 4.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 9000 | 5.0 | ❌ | Kernel below minimum |
| Cisco | NX-OS | Nexus 9000 | 6.0 | ❌ | Kernel below minimum |

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

### API Endpoint Role Security Matrix

| Method | Path | ROLE: system | ROLE: admin | ROLE: user | ROLE: api_result_read | ROLE: api_scan |
|--------|------|--------------|-------------|------------|-----------------------|----------------|
| GET | /auth | Y | Y | Y | Y | Y |
| GET | /version | Y | Y | Y | Y | Y |
| GET | /license | Y | Y | Y | Y | Y |
| POST | /license | Y | Y | | | |
| PUT | /license | Y | Y | | | |
| DELETE | /license | Y | Y | | | |
| POST | /license/refresh | Y | | | | |
| GET | /alerts/email | Y | Y | | | |
| GET | /alerts/email/:id | Y | Y | | | |
| POST | /alerts/email | Y | | | | |
| PUT | /alerts/email/:id | Y | | | | |
| DELETE | /alerts/email/:id | Y | | | | |
| POST | /alerts/email/test/:id | Y | | | | |
| GET | /alerts/syslog | Y | Y | | | |
| GET | /alerts/syslog/:id | Y | Y | | | |
| PUT | /alerts/syslog/:id | Y | | | | |
| POST | /alerts/syslog | Y | | | | |
| DELETE | /alerts/syslog/:id | Y | | | | |
| GET | /audit | Y | Y | | | |
| DELETE | /audit | Y | | | | |
| GET | /config | Y | | | | |
| PUT | /config | Y | | | | |
| GET | /credentials | Y | Y | Y | Y | |
| GET | /credentials/:id | Y | Y | Y | Y | |
| POST | /credentials/:id | Y | Y | | | |
| PUT | /credentials/:id | Y | Y | | | |
| GET | /hosts | Y | Y | Y | Y | |
| GET | /hosts/:id | Y | Y | Y | Y | |
| POST | /hosts | Y | Y | | | |
| POST | /hosts/retry | Y | Y | | | |
| PUT | /hosts/:id | Y | Y | | | |
| PUT | /hosts/tags | Y | Y | | | |
| GET | /hosts/:id/info/kernelmodules | Y | Y | Y | Y | |
| GET | /hosts/:id/info/lastlog | Y | Y | Y | Y | |
| GET | /hosts/:id/info/listeners | Y | Y | Y | Y | |
| GET | /hosts/:id/info/loggedinusers | Y | Y | Y | Y | |
| GET | /hosts/:id/info/processes | Y | Y | Y | Y | |
| GET | /hosts/:id/info/scheduledtasks | Y | Y | Y | Y | |
| GET | /hosts/:id/info/services | Y | Y | Y | Y | |
| GET | /hosts/:id/info/users | Y | Y | Y | Y | |
| GET | /hostsrollup/:id | Y | Y | Y | Y | |
| GET | /jumphosts | Y | Y | Y | Y | |
| GET | /jumphosts/:id | Y | Y | Y | Y | |
| POST | /jumphosts/:id | Y | Y | | | |
| PUT | /jumphosts/:id | Y | Y | | | |
| GET | /llmanalysis | Y | Y | | | |
| GET | /llmanalysis/:id | Y | Y | | | |
| POST | /llmanalysis | Y | Y | | | |
| PUT | /llmanalysis/:id/chat | Y | Y | | | |
| GET | /llmanalysis/:id/wait | Y | Y | | | |
| POST | /llmanalysis/bulkdelete | Y | Y | | | |
| GET | /notifications | Y | Y | | | |
| GET | /notifications/:id | Y | | | | |
| POST | /notifications | Y | | | | |
| PUT | /notifications/:id | Y | | | | |
| PUT | /notifications/pause/:id | Y | | | | |
| PUT | /notifications/unpause/:id | Y | | | | |
| POST | /notifications/test/:id | Y | | | | |
| GET | /reports/host_snapshot | Y | Y | | | |
| GET | /reports/scan_performance | Y | Y | | | |
| GET | /results/:id | Y | Y | Y | | |
| POST | /results | Y | Y | Y | | |
| POST | /results/timeline | Y | Y | Y | | |
| GET | /results/getMaxID | Y | Y | Y | | |
| POST | /results/delete/hostsandflies | Y | Y | | | |
| POST | /results/delete/sandflyhosts | Y | Y | | | |
| GET | /resultprofiles | Y | Y | | | |
| GET | /resultprofiles/:id | Y | Y | | | |
| GET | /resultprofiles/:id/sandfly/:sandfly | Y | Y | | | |
| POST | /resultprofiles/:id/sandfly/:sandfly/deleteresults | Y | Y | | | |
| PUT | /resultprofiles/:id | Y | Y | | | |
| GET | /resultprofiles/host/:hostid | Y | Y | | | |
| POST | /resultprofilesDelete | Y | Y | | | |
| POST | /resultprofiles | Y | Y | | | |
| POST | /resultprofiles/:id/append | Y | Y | | | |
| POST | /resultprofiles/:id/deletesandflies | Y | Y | | | |
| PUT | /resultprofiles/autodrift/:id/restartgather | Y | Y | | | |
| PUT | /resultprofiles/autodrift/:id/enforce | Y | Y | | | |
| PUT | /resultprofiles/autodrift/:id | Y | Y | | | |
| GET | /resultssummary/host/:hostid | Y | Y | Y | | |
| GET | /resultsummary/sandfly/:sandfly | Y | Y | Y | | |
| GET | /sandflies | Y | Y | Y | Y | |
| GET | /sandflies/name/:id | Y | Y | Y | Y | |
| PUT | /sandflies/name/:id/activate | Y | Y | | | |
| PUT | /sandflies/name/:id/deactivate | Y | Y | | | |
| PUT | /sandflies/activate | Y | Y | | | |
| PUT | /sandflies/deactivate | Y | Y | | | |
| POST | /sandflies | Y | Y | | | |
| PUT | /sandflies | Y | Y | | | |
| PUT | /sandflies/response/:id | Y | Y | | | |
| GET | /sandflies/backup | Y | Y | | | |
| POST | /sandflies/reload_all | Y | Y | | | |
| GET | /savedviews | Y | Y | | | |
| GET | /savedviews/:namespace | Y | Y | | | |
| POST | /savedviews | Y | Y | | | |
| POST | /scan | Y | Y | Y | Y | Y |
| POST | /scan/adhoc | Y | Y | Y | Y | Y |
| GET | /schedule | Y | Y | | | |
| GET | /schedule/:id | Y | Y | | | |
| POST | /schedule | Y | Y | | | |
| PUT | /schedule/:id | Y | Y | | | |
| PUT | /schedule/:id/abort | Y | Y | | | |
| PUT | /schedule/pause/:id | Y | Y | | | |
| PUT | /schedule/unpause/:id | Y | Y | | | |
| POST | /schedule/run/:id | Y | Y | | | |
| POST | /sharedurl | Y | Y | | | |
| GET | /sshhunter/summary | Y | Y | Y | Y | |
| GET | /sshhunter/minisummary | Y | Y | Y | Y | |
| GET | /sshhunter/key/:id | Y | Y | Y | Y | |
| PUT | /sshhunter/key/:id/tags | Y | Y | Y | | |
| PUT | /sshhunter/key/tags | Y | Y | Y | | |
| GET | /sshhunter/users | Y | Y | Y | Y | |
| GET | /sshhunter/users/:username | Y | Y | Y | Y | |
| GET | /sshhunter/hosts | Y | Y | Y | Y | |

---
## Features

### 🛡️ Core Capabilities

| Feature | Description |
|--------|-------------|
| 🚨 Security Alarms | Pass, alert, and error results from enabled Sandflies |
| 🖥️ Host Inventory | Hosts managed by the Sandfly Server |
| 🌐 Sandflies | Active Sandflies managed by the Sandfly Server |
| 🔑 SSH Hunter Data | SSH keys, users, hosts, and zones |
| 📋 Audit Logs | Sandfly Server system audit logs |
| ❗ Error Logs | Sandfly Server scanning and operational error logs |

### 📈 Analysis and Usage

| Feature | Description |
|--------|-------------|
| 📊 Dashboards | Visual analysis of Sandfly alarms and activity |
| 🔍 Suspicious Activity Review | Review of Sandfly-detected activity |
| 🧩 Splunk Search | Use Sandfly data in custom Splunk searches |
| 🧠 Anomaly Detection | Build anomaly detection models using Sandfly data |
| ⚙️ Incident Response | Support investigations using Sandfly events |

---

## Data Ingestion

The Sandfly Security for Splunk App retrieves data from a Sandfly Security server using the Sandfly Security REST API.

Data is ingested into a Splunk index specified during configuration. Each dataset retrieved from the Sandfly server is assigned a predefined sourcetype by the app. Events are stored in Splunk as JSON-formatted data.

---

## Server Connection Requirements

To ingest events from a Sandfly Security server, the following configuration items are required:

1. Sandfly Server URL  
2. Login Username  
3. Login Password  

These credentials are used to authenticate API requests to the Sandfly Security server.

---

## Supported Sourcetypes

The following sourcetypes are supported and assigned by the app:

| Sourcetype | Description |
|-----------|-------------|
| sandfly:alarms | Sandfly alarms including pass, alert, and error results |
| sandfly:hosts | Hosts managed by the Sandfly Server |
| sandfly:sandflies | Active Sandflies managed by the Sandfly Server |
| sandfly:ssh:keys | SSH Hunter keys, users, hosts, and zones |
| sandfly:logs:audit | Sandfly Server audit logs |
| sandfly:logs:error | Sandfly Server error and scanning logs |

---

## Dashboards

| Dashboard | Description |
|----------|-------------|
| 🧭 Overview | Summary of Sandfly activity and metrics |
| 🚨 Alarms | Sandfly alarm results |
| 🖥️ Hosts | Linux host inventory |
| 🔑 SSH Keys | SSH Hunter analysis |
| 📈 Metrics | Software and hardware metrics |
| 📋 Logs | Audit and error log visibility |

---

## Installation

### Step 1: Install the App

1. Download the Sandfly Security for Splunk App package  
2. In Splunk Web, navigate to Apps → Manage Apps  
3. Select Install app from file  
4. Upload the application package  
5. Restart Splunk if prompted  

---

### Step 2: Configure the App

1. Navigate to Apps → Sandfly Security → Setup  
2. Enter the Sandfly Server URL  
3. Enter the login username and password  
4. Select the target Splunk index for data ingestion  

---

### Step 3: Verify Data Collection

Run the following search to confirm data ingestion:

    index=<your_index> sourcetype=sandfly:*
    | stats count by sourcetype

---

## Directory Structure
```
Sandfly_Security_For_Splunk_App/
├── app.manifest
├── LICENSE
├── README.md
├── default/
│   ├── app.conf
│   ├── inputs.conf
│   ├── props.conf
│   ├── transforms.conf
│   ├── macros.conf
│   ├── restmap.conf
│   ├── savedsearches.conf
│   ├── web.conf
│   └── data/
│       └── ui/
│           ├── nav/
│           │   └── default.xml
│           └── views/
│               ├── setup.xml
│               ├── sandfly_overview.xml
│               ├── sandfly_results.xml
│               ├── sandfly_hosts.xml
│               ├── sandfly_sandflies.xml
│               ├── sandfly_sshhunter.xml
│               ├── sandfly_scans.xml
│               ├── sandfly_schedules.xml
│               ├── sandfly_notifications.xml
│               ├── sandfly_reports.xml
│               ├── sandfly_audit.xml
│               ├── sandfly_drift_detection.xml
│               ├── sandfly_ai_analysis.xml
│               ├── sandfly_jumphosts.xml
│               ├── sandfly_credentials.xml
│               ├── sandfly_whitelists.xml
│               ├── sandfly_settings.xml
│               ├── sandfly_operations.xml
│               ├── sandfly_logging.xml
│               └── sandfly_help.xml
├── bin/
│   ├── sandfly_input.py
│   ├── sandfly_setup_handler.py
│   └── sandfly_validation.py
├── metadata/
│   ├── default.meta
│   └── local.meta
└── static/
    ├── appIcon.png
    └── appIcon_2x.png
```

---

## Requirements

- Splunk Enterprise or Splunk Cloud
- Network connectivity to a Sandfly Security server
- Valid Sandfly Security credentials
- Sandfly Security platform deployed and operational

---

## ✅ AppInspect Compliance

- Proper Splunk directory structure
- Inputs disabled by default
- No hardcoded credentials
- Secure credential storage
- Raw JSON ingestion
- MIT License

---

## Reference

- Sandfly Security product documentation
  https://docs.sandflysecurity.com

- OAS Link: https://docs.sandflysecurity.com/v5.6.0/openapi/openapi-public.yaml🡵
- Splunk documentation: https://docs.splunk.com

---

## MIT License

Sandfly Security, Ltd.  https://www.sandflysecurity.com

#Copyright (c) 2026 Mark Teicher

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

