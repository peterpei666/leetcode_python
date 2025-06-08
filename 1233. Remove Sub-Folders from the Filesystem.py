class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ret = []
        folders = set(folder)
        for f in folder:
            sub = False
            prefix = f
            while prefix != '':
                pos = prefix.rfind('/')
                if pos== -1:
                    break
                prefix = prefix[:pos]
                if prefix in folders:
                    sub = True
                    break
            if not sub:
                ret.append(f)
        return ret
