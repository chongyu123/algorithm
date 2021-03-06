# Banary Search

l=[1,2,3,4,6,8,9,11,13,15,17,19,23,25,27,29,30,34,35,36,38,39,40,42,43,46,48,50]

def search(n):
    result = search_iter(n, 0, len(l)-1)
    return result

def search_iter(n, s_idx, e_idx):
    print "searching index ranges:", s_idx, e_idx

    if (n == l[s_idx]):
        return s_idx
        
    if (n == l[e_idx]):
        return e_idx

    if (e_idx - s_idx <= 1):
        return None

    m_idx = int((e_idx-s_idx)/2) + s_idx
    if (n == l[m_idx]):
        return m_idx
    
    if (n > l[m_idx]):
        return search_iter(n, m_idx, e_idx-1)
    else:
        return search_iter(n, s_idx+1, m_idx)

print search(5)