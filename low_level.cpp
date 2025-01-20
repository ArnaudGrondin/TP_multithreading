#include <Eigen/Dense>
#include <chrono>
#include <cpr/cpr.h>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>

using Eigen::MatrixXf;
using Eigen::VectorXf;
// using namespace::string
using json = nlohmann::json;
using namespace nlohmann::literals;
class Task {
private:
  /* data */
public:
  int identifier;
  int size;
  MatrixXf a;
  VectorXf b;
  VectorXf x;
  double time;

  Task(int identifier, int size);
  void work();
  std::string to_json();
  static Task from_json(std::string str);
  ~Task();
};

Task::Task(int identifier = 0, int size = 3) {
  identifier = identifier;
  size = size;
  a = MatrixXf::Random(size, size);
  b = VectorXf::Random(size);
  x = VectorXf::Zero(size);
  float time = 0.0;
}

void Task::work() { // on lance le travail de la tache et on mesure le temps de
                    // calcul
  std::chrono::steady_clock::time_point start =
      std::chrono::steady_clock::now();
  x = a.lu().solve(b);

  std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
  // time = double(end - start); TODO essayer de le convertir en float
  std::chrono::duration<double> diff =
      std::chrono::duration_cast<std::chrono::duration<double>>(end - start);

  std::cout << "Temps calcul  = " << diff.count() << "\n";
}

Task Task::from_json(std::string str) {
  // on recupere les données sous format json
  json j = json::parse(str);
  Task t = Task(j["identifier"], j["size"]);

  // Initialiser la matrice a
  auto a_data = j["a"];
  // t.a.resize(t.size, t.size); // Redimensionne la matrice
  for (int i = 0; i < t.size; ++i) {
    for (int j = 0; j < t.size; ++j) {
      t.a(i, j) = a_data[i][j];
    }
  }

  // Initialiser le vecteur b
  auto b_data = j["b"];
  // t.b.resize(t.size);
  for (int i = 0; i < t.size; ++i) {
    // std::cout << "b_data:\n" << b_data[i]<< "\n";
    t.b(i) = b_data[i];
  }

  return t;
}

Task::~Task() {}

int main() {

  std::cout << "hello" << std::endl;

  cpr::Response r = cpr::Get(cpr::Url{"127.0.0.1:8000"});
  std::string str = r.text;

  // //Simulation d'une réponse JSON
  //   std::string simulated_json = R"(
  //   {
  //       "identifier": 1,
  //       "a": [[1.0, 2.0], [3.0, 4.0]],t
  //       "b": [5.0, 6.0],
  //       "size": 2,

  //   })";

  // Initialisation depuis JSON
  // std::cout << "STRING :\n" << str << "\n";
  Task t = Task::from_json(str);

  // std::cout << "Matrice a:\n" << t.a << "\n";
  // std::cout << "Vecteur b:\n" << t.b << "\n";

  t.work(); // Résolution

  return 0;
} // TODO : FAIRE UN README pour les résultats,comparer different solver eigen
// TODO : COMPILER EN MODE RELEASE (trouver le bon parametre cmake build type
// (en CLI))
