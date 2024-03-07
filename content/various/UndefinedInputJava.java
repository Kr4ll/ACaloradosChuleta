// Cuando no hay un input definido y ademas no queremos perder lo consumido
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

// Cuando no hay un input definido y lo consumido no nos interesa
while (fastReader.hasNext().getKey()) {
	List<Integer> list = Arrays.stream(fastReader.nextLine().split(" "))
		.map(Integer::parseInt).collect(Collectors.toList());
}
fastReader.close();

