class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        visits = []
        for i in cpdomains:
            doms = i.split(" ")
            hits = int(doms[0])
            addr = doms[1]
            while "." in addr:
                if addr in res:
                    res[addr] += hits
                else:
                    res[addr] = hits
                addr = addr.split(".", 1)[1]
            if addr in res:
                res[addr] += hits
            else:
                res[addr] = hits
        for key in res.keys():
            visits.append(str(res[key]) + " " + key)
        return visitsS