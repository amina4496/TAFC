import random

def keygen(pk, msk, attr_list):
    r = random.randrange(1,ZR)
    g1_r = pk['g1'] ** r
    beta_inverse = 1 / msk['beta']
    k0 = (msk['g1_alpha'] * g1_r) ** beta_inverse
    K = {}
    for attr in attr_list:
        r_attr = random.randrange(1,ZR)
        k_attr1 = g1_r * (hash(str(attr)) ** r_attr)
        k_attr2 = pk['g2'] ** r_attr
        K[attr] = (k_attr1, k_attr2)

    return {'attr_list': attr_list, 'k0': k0, 'K': K}


def encryp(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   return result
#check the above function


def enc(pk, msg, policy_str):
    u=[]
    ZR=13
    n=len(policy_str)
    print "len(policy_str)==",n
    rand = random.randrange(1,ZR)
    #       u.append(rand)
    #s=u[0]  # shared secret
    c0 = pk['h'] ** rand
    crypto = encryp(msg,c0)
    return crypto
    
    
    
def setup():
    ZR=13
    G1=random.randrange(2,10)
    G2=random.randrange(2,10)
    
    g1 = random.randrange(1,G1)
    g2 = random.randrange(1,G2)

    beta = random.randrange(1,ZR)
    h = g2 ** beta
    
    f = g2 ** (1/beta)

    alpha = random.randrange(1,ZR)
    g1_alpha = g1 ** alpha
    e_gg_alpha = (g1_alpha, g2)

    pk = {'g1': g1, 'g2': g2, 'h': h, 'f': f ,'e_gg_alpha': e_gg_alpha}
    msk = {'beta': beta, 'g1_alpha': g1_alpha}
    return pk, msk
