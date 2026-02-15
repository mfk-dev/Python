# Base Class
class Security:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def scan(self):
        print(f"Scanning {self.target_ip} for vulnerabilities...")

# Child Class
class BugBounty(Security):
    def __init__(self, target_ip, reward):
        super().__init__(target_ip)
        self.reward = reward

    def claim_reward(self):
        print(f"Claiming a reward of ${self.reward} for finding vulnerabilities on {self.target_ip}!")

bug_bounty = BugBounty("192.168.1.100", 250)
bug_bounty.scan()
bug_bounty.claim_reward()
