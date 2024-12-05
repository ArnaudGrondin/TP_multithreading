#include <cpr/cpr.h>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

int main() {
  // using json = nlohmann::json;
  std::cout << "hello" << std::endl;

  cpr::Response r = cpr::Get(cpr::Url{"127.0.0.1:8000"});

  std::cout << r.text << std::endl;
  // std::ifstream f("example.json");

  return 0;
}
