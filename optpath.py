#!/usr/bin/env python
"""
coding=utf-8

Code Template

"""

import numpy as np
import os



# def main():
#     """
#     Main function documentation template
#     :return: None
#     :rtype: None
#     """
#     logging.getLogger().setLevel(logging.INFO)
# 
#     # Extract data from upstream.
#     observations = extract()
# 
#     # Spacy: Spacy NLP
#     nlp = spacy.load('en')
# 
#     # Transform data to have appropriate fields
#     observations, nlp = transform(observations, nlp)
# 
#     # Load data for downstream consumption
#     load(observations, nlp)
# 
#     pass


# def text_extract_utf8(f):
#     try:
#         return unicode(textract.process(f), "utf-8")
#     except UnicodeDecodeError, e:
#         return ''


def find_nn(coordsXY, nnn):
    '''Finds nearest neighbor cities to each city (including the city itself).
    
    Parameters:
    coordsXY (array): xy coordinates of the cities in the form [[x_1, y_1], [x_2, y_2], ...]
    nnn (int):  number of nearest neighbors to find
    
    Returns:  
    array: Array of nearest neighbors.  

    '''
    
    if os.path.isfile('nn_array_'+str(nnn)+'.npy'):
        nn_array = np.load('nn_array_'+str(nnn)+'.npy')
        
    else:
        nn_array = np.array([])
        for a in range(len(coordsXY)):
            if a%1000 == 0:
                print 'Percent computed: ' + str(a/float(len(coordsXY)))
            
            # coordinate differences [[x_a - x_1, y_a - y_1], [x_a - x_2, y_a - y_2], ... ]
            dist=(coordsXY - coordsXY[a]) 
            dist_square = np.multiply(dist,dist)
            closest = np.argpartition(dist_square[:,0]+dist_square[:,1],nnn) # nnn closest cities
            nn_array = np.append(nn_array, closest[:nnn]) 

        nn_array = nn_array.reshape((len(df),nnn)).astype(int)
        np.save('nn_array_'+str(nnn), nn_array)
    return nn_array

def delta_pure(path,coordsXY,(p,q)):
    '''Computes change in pure length of path after deformation.'''
    
    if p > q:
        p += 1
    
    d1 = np.linalg.norm(coordsXY[path[p-1]] - coordsXY[path[p]])
    d2 = np.linalg.norm(coordsXY[path[q-1]] - coordsXY[path[q]])
    d3 = np.linalg.norm(coordsXY[path[q]] - coordsXY[path[q+1]])

    d4 = np.linalg.norm(coordsXY[path[p-1]] - coordsXY[path[q]])
    d5 = np.linalg.norm(coordsXY[path[q]] - coordsXY[path[p]])
    d6 = np.linalg.norm(coordsXY[path[q-1]] - coordsXY[path[q+1]])
    
    return -(d1+d2+d3)+(d4+d5+d6)

def med_len(path, coordsXY):

    coord_diff = coordsXY[path][0:-1]-coordsXY[path][1:]
    coord_diff_sq = np.multiply(coord_diff, coord_diff)
    dists = np.sqrt(coord_diff_sq[:,0]+coord_diff_sq[:,1])
    return np.median(dists)

def make_deform(path,(p,q)):
    
    '''deform path by removing point at position q and inserting it at
    position p (!! position p in the list with q removed !!)'''
    
    # remove point at position q in path (q+1 => q, etc.)
    new_path = np.delete(path, q)
    
    if p > q: 
        
        # Point q was behind p on the path.
        # Insert path[q] at position p in new_path.
        # So for this case p => p-1 => p-1
        
        # [... q-1, q, q+1, ..., p-1, p, p+1]
        #--------------------------------------
        # [... a,   b, c,...   , e,   f, g]
        # remove path[q] => 
        # [... a,   c,...   , e, f,   g]
        # insert at p in new_path => 
        # [... a,   c,...   , e, f,   b, g]
        
        new_path = np.insert(new_path, p, path[q])
        
    else:
        # Point q was ahead of p on the path.  
        # Insert path[q] at position p in new_path.
        # So for this case p => p => p+1
        
        
        # [... p-1, p, p+1, ..., q-1, q, q+1]
        #--------------------------------------
        # [... a,   b, c,...   , e,   f, g, ...]
        # remove path[q] => 
        # [... a,   b, c,...   , e,   g, ...]
        # insert at p in new_path => 
        # [... a,   f, b, c,...     , e,   g, ...]
        
        
        new_path = np.insert(new_path, p, path[q])
    
    # Note in both cases new_path[min(p,q):max(p,q)+1] is the only
    # part of the list that is modified.  i.e. from position q to p 
    # *inclusive* for q < p (the +1 is just from slicing convention).  
    return new_path


# Main section
if __name__ == '__main__':
    main()
