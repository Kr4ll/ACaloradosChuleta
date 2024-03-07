/**
 * Author: Alberto Dekeno
 * License: CC0
 * Source: Codeforces
 * Description: Para numero de entradas indeterminadas 
 * Time: no time
 * Status: no tested
 */

 	boolean hayEntrada = true;
        while (hayEntrada) {
            Map.Entry<Boolean, Optional<String>> hasNextObject = fastReader.hasNext();
            hayEntrada = hasNextObject.getKey();
            if (hayEntrada) {
		//Haciendo hasNextObject.getValue() obtenemos el valor que consumio el hasNext
                List<Integer> list = Arrays.stream(hasNextObject.getValue().get().split(" "))
                        .map(Integer::parseInt).collect(Collectors.toList());
            }
        }
        fastReader.close();

        while (fastReader.hasNext().getKey()) {
                //En este caso lo consumido por hasNext no nos interesa
                List<Integer> list = Arrays.stream(fastReader.nextLine().split(" "))
                        .map(Integer::parseInt).collect(Collectors.toList());
        }
        fastReader.close();

