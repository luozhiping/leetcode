# 648. 单词替换
# https://leetcode-cn.com/problems/replace-words/

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        class TreeNode(object):
            def __init__(self, char, isWord = False):
                self.char = char
                self.isWord = isWord
                self.children = {}

        def buildTree(root, word):
            if len(word) == 0:
                return
            treeNode = TreeNode(word[0], len(word) == 1)
            if word[0] in root.children:
                if treeNode.isWord:
                    root.children[word[0]].isWord = True
            else:
                root.children[word[0]] = treeNode
            buildTree(root.children[word[0]], word[1:])

        root = TreeNode("")
        for word in dict:
            buildTree(root, word)

        words = sentence.split(' ')
        result = []

        def findPreix(root, word, prefix = ''):
            if len(word) == 0:
                return ""
            if word[0] in root.children:
                prefix = prefix + word[0]
                if root.children[word[0]].isWord:
                    return prefix
                return findPreix(root.children[word[0]], word[1:], prefix)
            else:
                return ""

        result = []
        for word in words:
            pre = findPreix(root, word)
            if len(pre) == 0:
                result.append(word)
            else:
                result.append(pre)
        return ' '.join(result)



s = Solution()
print(s.replaceWords(["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"],
"ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"))