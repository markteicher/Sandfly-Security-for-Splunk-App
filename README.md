# Sandfly Security for Splunk App

## Overview

Sandfly Security is an agentless intrusion detection and incident response platform for Linux. 

Sandfly Security automatically analyzes Linux hosts for intruders 24 hours a day without loading any software on endpoints. 

Sandfly Security retrieves security, hardware, operating system, and related system data from Linux hosts and makes this data available for analysis. Sandfly operates across virtually all Linux distributions immediately and is designed to function without introducing risk to system stability or performance.

The Sandfly Security for Splunk App is a single Splunk application that ingests events from a Sandfly Security server using the Sandfly Security REST API. The app ingests data into a user-specified Splunk index and assigns the correct sourcetype to each event. All events are ingested in JSON format to preserve the original structure and content of the Sandfly data.

The Splunk app provides dashboards, reports, and search logic for analyzing data ingested from a Sandfly Security server. 

This includes Sandfly Security alarms, suspicious activity results, SSH Hunter data, host inventory, and Sandfly server audit and error logs. 

Data retrieved by Sandfly Securitu can also be used by Splunk users to build searches, reports, anomaly detection models, and incident response workflows within Splunk.

The Splunk App is intended to surface Sandfly data directly inside Splunk so that Asset Owners and operational teams can view, analyze and action Sandfly Security results without requiring access to the Sandfly Security user interface.


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
| Arch Linux | Rolling (kernel ≥ 2.6.32) | Rolling | ✅ |
| Gentoo | Rolling (kernel ≥ 2.6.32) | Rolling | ✅ |

### Cloud & Virtualization Platforms (Kernel ≥ 2.6.32)

| Platform | Supported |
|---------|-----------|
| Amazon Linux | ✅ |
| DigitalOcean Linux images | ✅ |
| Microsoft Azure Linux images | ✅ |

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


### Network & Embedded Devices (Kernel ≥ 2.6.32)

| Platform | Description | Supported |
|---------|-------------|-----------|
| Cisco network devices | Linux-based operating systems on Cisco network platforms | ✅ |
| Juniper network devices | Linux-based operating systems on Juniper network platforms | ✅ |
| Embedded Linux systems | Embedded and appliance-based Linux systems, including devices such as Raspberry Pi | ✅ |

---
⚠️ Disclaimer

These tools are not official Sandfly Security products or utilities

Use of this software is not covered by any license, warranty, or support agreement you may have with Sandfly
Security.

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

## App Structure

Sandfly_Security_For_Splunk_App/
  app.manifest
  LICENSE
  README.md
  default/
    app.conf
    inputs.conf
    indexes.conf
    props.conf
    transforms.conf
    savedsearches.conf
    data/ui/
      nav/
      views/
  bin/
  metadata/
  static/

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

