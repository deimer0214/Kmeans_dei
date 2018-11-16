import math
import random
import operator

# This methods create k random points.
def puntos_aleatorios(clusters, dimension, valor_maximo):
        resultado = list()
        for i in range(1, clusters + 1):
                punto = list()
                for j in range(dimension):
                        punto.append(
                                random.randrange(1,
                                                 valor_maximo))
                resultado.append(punto)
        return resultado

# This method calculates the dist_euclidea Distance between two lists.
def dist_euclidea(lista1, lista2):
    suma_vector = 0
    for i in range(len(lista1)):
            suma_vector += pow((lista1[i] - lista2[i]), 2)
    return math.sqrt(suma_vector)

# This method find the closet center for the given point.
def hallar_centro(punto, centros):
        distancias = dict()
        for centro in centros:
                distancias[repr(centro)] = dist_euclidea(punto, centro)
        return sorted(distancias .items(),
                      key=operator.itemgetter(1),
                      reverse=True)[0][0]

# This method creates a dict of empty lists for each dick key.
def listas_vacias(centros):
        resultado = dict()
        for centro in centros:
                resultado[repr(centro)] = list()
        return resultado

# This method returns whether a dict has an empty list() as value.
def lista_vacia_defecto(lista1):
        for elemento in lista1:
                if len(lista1[elemento]) == 0:
                        return True
        return False

# This method creates a dict of size n whose values are empty-lists.
def creacion_listas(largo):
        resultado = dict()
        for i in range(largo):
                resultado[i] = list()
        return resultado

# This method creates process the data by grouping the values
# per dimension.
def agrupando_dimension(datos, dimension):
        dim_dict = creacion_listas(dimension)
        for elemento in datos:
                for i in range(dimension):
                        dim_dict[i].append(elemento[i])
        return dim_dict


# This method calculate de center for the given given points
# as assignation and dim_dict.
def asigna_new_centro(assignation, dim_lista):
        center = list()

        if not lista_vacia_defecto(dim_lista):
                for d in range(len(dim_lista.keys())):
                        center.append(
                                sum(dim_lista[d]) / len(dim_lista[d]))
        else:
                for d in range(len(dim_lista.keys())):
                        center.append(
                                eval(assignation)[d])
        return center

# This method performs the update algorithm step for the given
# assignations and the dimension.
def actualizacion_paso_n(asignaciones, dim):
        centers = list()
        for asignacion_new in asignaciones:
                centers.append(
                        asigna_new_centro(asignacion_new,
                                         agrupando_dimension(
                                                 asignaciones[asignacion_new],
                                                dim)))
        return centers


# This method develops the assignation step of the algorithm.
def asignacion_paso_n(puntos, centros):
        assignation_lista = listas_vacias(centros)
        for punto in puntos:
                assignation_lista[
                        hallar_centro(punto,
                                      centros)].append(punto)
        return assignation_lista


# This method performs the k-means algorithm for
# the given data and for the given iterations.
def excecuter(datos, clusters, iteraciones, dim, numero_max):
	centros = puntos_aleatorios(clusters, dim, numero_max)
	for i in range(iteraciones):
            centros = actualizacion_paso_n(
			asignacion_paso_n(datos, centros),
			len(datos[0]))
	return asignacion_paso_n(datos, centros)



# data = ([1,1,11],
#         [1,3,2],
#         [2,4,5],
#         [2,2,53],
#         [2,3,25],
#         [8,6,81],
#         [7,4,18],
#         [9,6,88],
#         [7,5,103],
#         [5,8,45],
#         [4,4,24],
#         [4,5,83],
#         [5,3,7],
#         [6,6,19])

data = ([1,1],
        [1,3],
        [2,4],
        [2,2],
        [2,3],
        [8,6],
        [7,4],
        [9,6],
        [7,5],
        [5,8],
        [4,4],
        [4,5],
        [5,3],
        [6,6])

k = 3
iterations = 14
dim = 2
maxNumberValue = 9

#ejecución del code principal
kClusters = excecuter(data, k, iterations, dim, maxNumberValue)

print(kClusters)