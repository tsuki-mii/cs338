import hashlib

def encrypt_str(str):
    sha = hashlib.sha256(str.encode()).hexdigest()
    return sha
# part 3
words = [line.strip().lower() for line in open('words.txt')]
print(len(words))
pwds = [line.strip().lower() for line in open('passwords3.txt')]
i = 0
while i < 50:
    for w in words:
        if pwds[i].split('$')[3][:-14] == encrypt_str(pwds[i].split('$')[2] + w):
            print(pwds[i].split('$')[0] + w)
    i += 1
# part 1
og_words = [line.strip().lower() for line in open('words.txt')]
i = 0
pwds = [line.strip().lower() for line in open('passwords1.txt')]
pwds2 = [line.strip().lower() for line in open('passwords1.txt')]
for w in words:
    words[i] = encrypt_str(w)
    i += 1
i = 0
for p in pwds:
    pwds[i] = p.split(':')[1]
    i += 1
j = 0
i = 0
for p in pwds:
    for w in words:
        if p == w:
            print(pwds2[i].split(':')[0] + ':' + og_words[j])
        j += 1
    j = 0
    i += 1