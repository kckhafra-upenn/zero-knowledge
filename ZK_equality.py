from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    r1 = Secrete(utils.get_random_num(bits=128))
    r2 = Secrete(utils.get_random_num(bits=128))
    #Generate a NIZK proving equality of the plaintexts
    m=1
    C1 = r1.value * GamalC2 = m * G + r1.value *H
    C2 = m*G + r1.value * H
    #Return two ciphertexts and the proof
    D1 = r2.value*G
    D2 = m*G+r2.value *H
    return (C1,C2), (D1,D2), zk_proof

