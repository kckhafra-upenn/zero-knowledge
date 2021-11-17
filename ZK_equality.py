from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    r1 = Secret(utils.get_random_num(bits=128))
    r2 = Secret(utils.get_random_num(bits=128))
    print(r1,r2)
    #Generate a NIZK proving equality of the plaintexts
    m=1
    C1 = r1.value * G
    C2 = r1.value * H + m *G
    #Return two ciphertexts and the proof
    D1 = r2.value*G
    D2 = m*G+r2.value *H
    return (C1,C2), (D1,D2), zk_proof

# # Setup: Peggy and Victor agree on two group generators.
# G, H = utils.make_generators(num=2, seed=42)
