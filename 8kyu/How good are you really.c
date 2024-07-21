int better_than_average(int class_points[], int class_size, int your_points) {
  double point_sum = your_points;
  for (int i = 0; i < class_size; i++) {
    point_sum += class_points[i];
  }
  return your_points > (point_sum / (class_size + 1));
}