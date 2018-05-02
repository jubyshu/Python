# 元音字母 有：a，e，i，o，u五个， 写一个函数，交换字符串的元音字符位置。

# 假设，一个字符串中只有二个不同的元音字符。

# 二个测试用例：

# 输入 apple  输出 eppla

# 输入machin 输出 michan

def change_char(word):
	s = list(word)
	vowels = ['a', 'e', 'i', 'o', 'u']
	index = [s.index(vowel) for vowel in vowels if vowel in word]
	#print(index)
	s[index[0]], s[index[1]] = s[index[1]], s[index[0]]
	# for vowel in vowels:
	# 	if  vowel in word:
	# 		s = list(vowel)
	# return word
	return ''.join(s)

print(change_char('apple'))


def reverse_vowel(s):
    yuanyin = 'aeiou'
    L = []
    for i in range(len(s)):
        if s[i] in yuanyin:
            L.append(i)
    List = list(s)
    List[L[0]], List[L[1]] = s[L[1]], s[L[0]]
    return ''.join(List)
print(reverse_vowel('apple'))