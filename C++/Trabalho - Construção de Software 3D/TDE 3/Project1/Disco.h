#pragma once
# define PI 3.141592653589793238462643383279502884L /* pi */
# define nTriangulos 8.0f  // Número de triângulos que compõem a circunferência.

class Disco
{
public:
	float pcx, pcy, pcz;
	float raio;       
	int id;

	Disco(int idC, float ppcx, float ppcy, float ppcz, float rraio);
	void Desenha();
	~Disco();
};
