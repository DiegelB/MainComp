#include <iostream>
using namespace std;

int main() {
	const double TOWN_MILAGE = 23.5, HIGHWAY_MILAGE = 28.9, TANK_SIZE = 20;
	double distance;

	//distance for town
	distance = TOWN_MILAGE * TANK_SIZE;
	cout << "You can drive " << distance << " miles when in town.\n";
	//distance for highway
	distance = HIGHWAY_MILAGE * TANK_SIZE;
	cout << "You can dive " << distance << " miles when on a highway\n";
	return 0;
}
