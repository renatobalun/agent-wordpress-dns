from llama_index.core.tools.tool_spec.base import BaseToolSpec

import requests



class DnsSpec(BaseToolSpec):
    """Dns Spec"""
    
    spec_functions = ["dns"]
    
    def dns(self, domain:str):
        "A tool for DNS record analysis. Tells if DNS records are okay for our site and instructs the user to change them if they are not valid. Call this tool if domain is mentioned in a prompt."
        
        dns_records = requests.get(f"https://dns-check.plus.hr/dns/{domain}")
        
        dns_records_json = dns_records.json()
        print(dns_records_json["NS"])
        required_ns_records=["dns1.registrar-servers.com","dns2.registrar-servers.com"]
        
        
        if set(required_ns_records) == set(dns_records_json["NS"]):
            analysis_result = {
            "ns_records": {
                "found": dns_records_json["NS"],
                "required": ["dns1.registrar-servers.com","dns2.registrar-servers.com"],
                "message": "The NS records are set correctly."
                }
            }
        else:
            analysis_result = {
            "ns_records": {
                "found": dns_records_json["NS"],
                "required": ["dns1.registrar-servers.com","dns2.registrar-servers.com"],
                "message": "The NS records are not set correctly. Please change to dns1.registrar-servers.com or dns2.registrar-servers.com."
                }
            }
        
        
        
        return {
                "domain": domain,
                "analysis": analysis_result,
                "raw_records": dns_records
            }
        
        
        