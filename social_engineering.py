#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import platform
import json
import random
from pathlib import Path

class SocialEngineering:
    def __init__(self):
        self.targets = []
        self.techniques = []
        self.results = []
        
    def generate_target_profiles(self):
        print("[+] Generating target profiles...")
        
        target_types = ["Employee", "Manager", "IT Staff", "Receptionist", "Security Guard"]
        departments = ["HR", "Finance", "IT", "Marketing", "Operations", "Sales"]
        
        for i in range(5):
            target = {
                "id": i + 1,
                "type": random.choice(target_types),
                "department": random.choice(departments),
                "vulnerability_score": random.randint(1, 10),
                "social_media_presence": random.choice([True, False]),
                "email_pattern": f"user{i+1}@company.com"
            }
            self.targets.append(target)
            print(f"    [+] Created target: {target['type']} from {target['department']}")
            
    def analyze_social_engineering_techniques(self):
        print("[+] Analyzing social engineering techniques...")
        
        techniques = [
            {"name": "Phishing", "effectiveness": 8, "difficulty": 3},
            {"name": "Pretexting", "effectiveness": 7, "difficulty": 4},
            {"name": "Baiting", "effectiveness": 6, "difficulty": 2},
            {"name": "Quid Pro Quo", "effectiveness": 5, "difficulty": 3},
            {"name": "Tailgating", "effectiveness": 4, "difficulty": 1},
            {"name": "Impersonation", "effectiveness": 9, "difficulty": 6},
            {"name": "Vishing", "effectiveness": 7, "difficulty": 4},
            {"name": "Watering Hole", "effectiveness": 6, "difficulty": 5}
        ]
        
        for tech in techniques:
            self.techniques.append(tech)
            
        print(f"    [+] Analyzed {len(self.techniques)} techniques")
        
    def simulate_phishing_attack(self):
        print("[+] Simulating phishing attack...")
        
        phishing_templates = [
            "Urgent: Your account has been compromised",
            "Important: System maintenance required",
            "Action required: Password expiration",
            "Security alert: Suspicious activity detected"
        ]
        
        for target in self.targets:
            if target["vulnerability_score"] > 5:
                template = random.choice(phishing_templates)
                success_rate = random.randint(60, 95)
                
                result = {
                    "target": target["id"],
                    "technique": "Phishing",
                    "template": template,
                    "success_rate": success_rate,
                    "risk_level": "HIGH" if success_rate > 80 else "MEDIUM"
                }
                
                self.results.append(result)
                print(f"    [+] Target {target['id']}: {success_rate}% success rate")
                
    def simulate_pretexting_attack(self):
        print("[+] Simulating pretexting attack...")
        
        pretexts = [
            "IT Support calling about system issues",
            "HR department requesting verification",
            "Security team conducting audit",
            "Vendor representative with urgent delivery"
        ]
        
        for target in self.targets:
            if target["department"] in ["IT", "HR"]:
                pretext = random.choice(pretexts)
                success_rate = random.randint(40, 85)
                
                result = {
                    "target": target["id"],
                    "technique": "Pretexting",
                    "pretext": pretext,
                    "success_rate": success_rate,
                    "risk_level": "HIGH" if success_rate > 70 else "MEDIUM"
                }
                
                self.results.append(result)
                print(f"    [+] Target {target['id']}: {success_rate}% success rate")
                
    def generate_attack_report(self):
        print("\n===============================================")
        print("    Social Engineering Attack Report")
        print("===============================================")
        
        print(f"Targets analyzed: {len(self.targets)}")
        print(f"Techniques available: {len(self.techniques)}")
        print(f"Attack simulations: {len(self.results)}")
        
        if self.targets:
            print("\nTarget Profiles:")
            for target in self.targets:
                print(f"{target['id']}. {target['type']} - {target['department']}")
                print(f"   Vulnerability Score: {target['vulnerability_score']}/10")
                print(f"   Social Media: {'Yes' if target['social_media_presence'] else 'No'}")
                print(f"   Email: {target['email_pattern']}")
                print()
                
        if self.results:
            print("\nAttack Results:")
            for result in self.results:
                print(f"Target {result['target']} - {result['technique']}")
                print(f"   Success Rate: {result['success_rate']}%")
                print(f"   Risk Level: {result['risk_level']}")
                if 'template' in result:
                    print(f"   Template: {result['template']}")
                if 'pretext' in result:
                    print(f"   Pretext: {result['pretext']}")
                print()
                
        self.save_report()
        
    def save_report(self):
        report_file = "social_engineering_report.json"
        
        report_data = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "author": "@Bengamin_Button",
            "team": "@XillenAdapter",
            "platform": platform.system(),
            "targets": self.targets,
            "techniques": self.techniques,
            "results": self.results,
            "summary": {
                "total_targets": len(self.targets),
                "total_techniques": len(self.techniques),
                "total_attacks": len(self.results),
                "high_risk_targets": len([t for t in self.targets if t['vulnerability_score'] > 7])
            }
        }
        
        try:
            with open(report_file, 'w') as f:
                json.dump(report_data, f, indent=2)
            print(f"[+] Report saved to: {report_file}")
        except Exception as e:
            print(f"[-] Error saving report: {e}")
            
    def run_social_engineering(self):
        print("===============================================")
        print("    XILLEN Social Engineering")
        print("    Социальная инженерия")
        print("===============================================")
        print("Author: @Bengamin_Button")
        print("Team: @XillenAdapter")
        print()
        
        self.generate_target_profiles()
        print()
        
        self.analyze_social_engineering_techniques()
        print()
        
        self.simulate_phishing_attack()
        print()
        
        self.simulate_pretexting_attack()
        print()
        
        self.generate_attack_report()

def main():
    se = SocialEngineering()
    se.run_social_engineering()

if __name__ == "__main__":
    main()
