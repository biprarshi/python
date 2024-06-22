import array

print(array.typecodes)   #Kinds of datatypes

array1 = array.array('i', [2, 4, 5, 77, 9])

print(array1)
print(array1.buffer_info())
print(type(array1))

array2 = array.array('i', range(51))
for ii in array2:
    print(ii, end=' ')
print()

import datetime
print(datetime.datetime.now())
array3 = array.array('Q', range(1000000000))
print(array3)
print(array3[-1])
print(datetime.datetime.now())
# for ii in array3:
#     print(ii, end=' ')



# List of type codes

# Type code	C Type	            Python Type	        Minimum Size (Bytes)
# b	        signed char	        int	                1
# B	        unsigned char	    int	                1
# u	        Py_UNICODE	        Unicode Character 	2
# h	        signed short	    int	                2
# H	        unsigned short	    int	                2
# i	        signed int	        int	                2
# I	        unsigned int	    int	                2
# l	        signed long	        int	                4
# L	        unsigned long	    int	                4
# q	        signed long long	int	                8
# Q	        unsigned long long	int	                8
# f	        float	            float	            4
# d	        double	            float	            8