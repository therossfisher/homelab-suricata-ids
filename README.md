# Home Network Security Monitoring Stack
## Raspberry Pi 4 + Suricata 7 + DShield Honeypot

## Overview
A Raspberry Pi 4 running a full network security monitoring stack including 
Suricata IDS, DShield/ISC honeypot sensor, and AI-assisted alert triage.
Contributing real threat intelligence to the SANS Internet Storm Center.

## Hardware
- Raspberry Pi 4 Model B
- Connected via ethernet to home network switch
- Ubiquiti Dream Router with port mirroring and port forwarding

## Stack
- Raspberry Pi OS Lite 64-bit
- Suricata 7.0.10 with Emerging Threats Open Ruleset (50,143 rules)
- DShield Honeypot Sensor v99 (SANS ISC)
- Cowrie SSH Honeypot (port 22 exposed to internet)
- Python alert parser for human-readable triage output

## Status
- [x] Suricata installed and running
- [x] Rules loaded and verified
- [x] First alert generated
- [x] Python alert parser
- [x] DShield sensor registered with SANS ISC
- [x] Cowrie SSH honeypot internet-facing on port 22
- [x] Firewall configured and hardened
- [ ] Port mirroring for full network visibility
- [ ] Automated alerting
- [ ] Status dashboard

## Sensor Info
- External IP: 68.6.247.186
- ISC Sensor ID: 3000055796
- Reports: https://isc.sans.edu/myreports.html
