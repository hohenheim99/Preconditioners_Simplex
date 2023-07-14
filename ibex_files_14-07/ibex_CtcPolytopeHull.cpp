//============================================================================
//                                  I B E X
// File        : ibex_CtcPolytopeHull.cpp
// Author      : Gilles Chabert
// Copyright   : Ecole des Mines de Nantes (France)
// License     : See the LICENSE file
// Created     : Oct 31, 2013
// Last update : Aug 01, 2018
//============================================================================

#include "/home/nico/Ibex/ibex-2.8.9/src/contractor/ann.cpp"
// #include "/home/nico/Ibex/ibex-2.8.9/src/contractor/funtions_for_ANN.cpp"


#include "ibex_CtcPolytopeHull.h"
#include "ibex_LinearizerFixed.h"
#include "ibex_LinearizerXTaylor.h"
#include <iostream>
#include <fstream>
#include <chrono>
#include <list>


//Libraries para red
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>









using namespace std;
long double exec_simplex=0; 
long double exec_line=0;
long double exec_red=0;

namespace ibex {

namespace {

class PolytopeHullEmptyBoxException { };

}

CtcPolytopeHull::CtcPolytopeHull(Linearizer& lr, int max_iter, int time_out, double eps) :
		Ctc(lr.nb_var()), lr(lr),
		mylinearsolver(nb_var, LPSolver::Mode::Certified, eps, time_out, max_iter),
		contracted_vars(BitSet::all(nb_var)), own_lr(false), primal_sols(2*nb_var, nb_var),
		primal_sol_found(2*nb_var),P(0,0) {

}

CtcPolytopeHull::CtcPolytopeHull(const Matrix& A, const Vector& b, int max_iter, int time_out, double eps) :
		Ctc(A.nb_cols()), lr(*new LinearizerFixed(A,b)),
		mylinearsolver(nb_var, LPSolver::Mode::Certified, eps, time_out, max_iter),
		contracted_vars(BitSet::all(nb_var)), own_lr(true), primal_sols(2*nb_var, nb_var),
		primal_sol_found(2*nb_var),P(0,0) {

}

CtcPolytopeHull::~CtcPolytopeHull() {
	if (own_lr) delete &lr;
}

void CtcPolytopeHull::add_property(const IntervalVector& init_box, BoxProperties& map) {
	lr.add_property(init_box, map);
}

void CtcPolytopeHull::contract(IntervalVector& box) {
	ContractContext context(box);
	contract(box,context);
}

void CtcPolytopeHull::contract(IntervalVector& box, ContractContext& context) {
	primal_sol_found.clear();
	LinearizerXTaylor * lr2 = dynamic_cast<LinearizerXTaylor*>(&lr);
	if (box.is_unbounded()) return;

	try {
		using std::chrono::high_resolution_clock;
   		using std::chrono::duration_cast;
    	using std::chrono::duration;
    	using std::chrono::milliseconds;

		auto p1 = high_resolution_clock::now();
		int cont = lr2->linearize(box, mylinearsolver, context.prop); //returns the number of constraints in the linearized system
		auto p2 = high_resolution_clock::now();
		
		duration<double, std::milli> line_ms = p2 - p1;
		double temp2 =line_ms.count();
		exec_line+=temp2;
		
		

		if (cont==-1) throw PolytopeHullEmptyBoxException();

		if (cont==0) return;
		//------------------------------Red neronal-----------------------------
		auto red1=high_resolution_clock::now();
		// // string path="/home/nico/codes/modelos/MC-1/Modelo_MC-1_3m_final_/model.model";
		// string MC4="/home/nico/codes/modelos/MC-4/Modelo_MC-4_relu_3m_50epo/model.model";
	
		// vector<float> AXB_for_red;
		// for (int i=0;i<lr2->L_A.nb_rows();i++){
		// 			for (int k=0;k<lr2->L_A.nb_cols();k++){
		// 				AXB_for_red.push_back(lr2->L_A[i][k]);
		// 			}
		// 		}
		// for (int i=0;i<box.size();i++){
		// 			AXB_for_red.push_back(box[i].lb());
		// 			AXB_for_red.push_back(box[i].ub());

		// 	}
		// for (int i=0;i<lr2->L_b.size();i++){
		// 		AXB_for_red.push_back(lr2->L_b[i]);
		// 	}

		// // // float proba=Model_output_recommend(path,AXB_for_red,295);
		// // // float proba=1.0;
		// vector<float> output_ann=ANN_P(MC4,AXB_for_red,295);
		// int filas=lr2->L_A.nb_rows();
    	// std::vector<std::vector<float>> vectors_P=createVectors(output_ann,filas);
		
		// IntervalMatrix precondi(vectors_P.size(),filas);
		
		// for(int i = 0;i<vectors_P.size();i++){
		// 	for(int j=0;j<filas;j++){
		// 		precondi[i][j]=vectors_P[i][j];
		// 	}
		// }
		
		//  // m*n = n*p
	

		// IntervalMatrix PA= precondi * lr2->L_A;
		// IntervalVector Pb_aux = precondi*lr2->L_b;

		// IntervalVector Pb(Pb_aux.size());
		// for (int i = 0 ; i <Pb_aux.size() ; i++){
    	// 		Pb[i]=Interval(NEG_INFINITY,Pb_aux[i].ub());
		// }
	
		// if (!precondi.is_empty()){
		// 	bwd_mul(Pb,PA,box, 1e8);
		// }

		auto red2= high_resolution_clock::now();
		duration<double, std::milli> red_time_dif = red2 - red1;
		double red_time =red_time_dif.count();
		exec_red+=red_time;
		//----------------------------Red neuronal-----------------------------------
		IntervalVector aux =box; //copia de los intervalos
		//---------------------------Simplex--------------------------------
		
		P.resize(0,0);
		// if (proba >= 0.4){
		auto t1 = high_resolution_clock::now();
		optimizer(box);
		auto t2 = high_resolution_clock::now();
		duration<double, std::milli> ms_double = t2 - t1;
		double temp =ms_double.count();
		exec_simplex+=temp;
		// }
		
		

		
	
		//---------------------------Simplex--------------------------------
		
		// if((rand() % 100) <=101 && false){
		// 		int rows = box.size();
				
		// 		ibex::Vector diam_pre = aux.diam();
		// 		ibex::Vector diam_post = box.diam();
		// 		std::vector <double> diams;
		// 		for (int i=0;i<rows;i++){
		// 			double rate=((diam_pre[i]-diam_post[i])/diam_pre[i])*100;
		// 			diams.push_back(rate);
		// 		}
		// 		//SALIDA DEL SIMPLEX
		// 		std::ofstream Simplex_P;
		// 		Simplex_P.open("test_results/DS_P.txt",std::ios_base::app);
		// 		for (int i=0;i<P.nb_rows();i++){
		// 			for (int k=0;k<P.nb_cols();k++){
		// 				Simplex_P<<P[i][k]<<" ";
		// 			}
		// 		}
		// 		Simplex_P<<endl;
		// 		Simplex_P.close();

		// 		std::ofstream intervals_file;
		// 		intervals_file.open("test_results/intervals_change.txt",std::ios_base::app);
		// 		for (int i=0;i<diams.size();i++){intervals_file<< diams[i] << " ";}
		// 		intervals_file<<endl;
		// 		intervals_file.close();

		// 		std::ofstream AXB;
		// 		AXB.open("test_results/AXB.txt",std::ios_base::app);
		// 		for (int i=0;i<lr2->L_A.nb_rows();i++){
		// 			for (int k=0;k<lr2->L_A.nb_cols();k++){
		// 				AXB<<lr2->L_A[i][k]<<" ";
		// 			}
		// 		}
		// 		for (int i=0;i<aux.size();i++){ AXB<<aux[i]<<" ";}
		// 		for (int i=0;i<lr2->L_b.size();i++){AXB<<lr2->L_b[i]<<" ";}
		// 		AXB<<endl;
		// 		AXB.close();

		// }
		

		mylinearsolver.clear_constraints();
	}
	catch(PolytopeHullEmptyBoxException& e) {
		box.set_empty(); // empty the box before exiting
		mylinearsolver.clear_constraints();
	}

	context.prop.update(BoxEvent(box,BoxEvent::CONTRACT));

}

void CtcPolytopeHull::set_contracted_vars(const BitSet& vars) {
	contracted_vars = vars;
}

void CtcPolytopeHull::optimizer(IntervalVector& box) {

	Interval opt(0.0);
	int* inf_bound = new int[nb_var]; // indicator inf_bound = 1 means the inf bound is feasible or already contracted, call to simplex useless (cf Baharev)
	int* sup_bound = new int[nb_var]; // indicator sup_bound = 1 means the sup bound is feasible or already contracted, call to simplex useless

	for (int i=0; i<nb_var; i++) {

		if (contracted_vars[i]) {
			inf_bound[i]=0;
			sup_bound[i]=0;
		} else {
			inf_bound[i]=1;
			sup_bound[i]=1;
		}
	}

	int nexti=-1;   // the next variable to be contracted
	int infnexti=0; // the bound to be contracted contract  infnexti=0 for the lower bound, infnexti=1 for the upper bound
	LPSolver::Status stat=LPSolver::Status::Unknown;

	// Update the bounds the variables
	mylinearsolver.set_bounds(box);
	for(int ii=0; ii<(2*nb_var); ii++) {  // at most 2*n calls

		int i= ii/2;
		if (nexti != -1) i=nexti;
		//cout << "[polytope-hull]->[optimize] var n°"<< i << " infnexti=" << infnexti << " infbound=" << inf_bound[i] << " supbound=" << sup_bound[i] << endl;
		//cout << "[polytope-hull]->[optimize] box before simplex: " << box << endl;
		if (infnexti==0 && inf_bound[i]==0)  // computing the left bound : minimizing x_i
		{
			inf_bound[i]=1;
			mylinearsolver.set_cost(i, 1.0);
			stat = mylinearsolver.minimize();
			mylinearsolver.set_cost(i, 0.0);
			//cout << "[polytope-hull]->[optimize] simplex for left bound returns stat:" << stat << endl;
			if (stat == LPSolver::Status::OptimalProved) {
				opt = mylinearsolver.minimum();
				//std::cout << "opt=" << opt << endl;
				if(opt.lb()>box[i].ub()) {
					delete[] inf_bound;
					delete[] sup_bound;
					throw PolytopeHullEmptyBoxException();
				}
				primal_sols[2*i]=mylinearsolver.not_proved_primal_sol();
				primal_sol_found.add(2*i);

				if(opt.lb() > box[i].lb()) {
					Vector dual_vector = mylinearsolver.not_proved_dual_sol();
					P.resize(P.nb_rows()+1,dual_vector.size()-box.size());
					for (int i = box.size() ; i < dual_vector.size() ; i++){
						P[P.nb_rows()-1][i-box.size()] = -dual_vector[i];
					}
					box[i]=Interval(opt.lb(),box[i].ub());
					mylinearsolver.set_bounds(i,box[i]);
				}

				if (!choose_next_variable(box,nexti,infnexti, inf_bound, sup_bound)) {
					break;
				}
			}
			else if (stat == LPSolver::Status::InfeasibleProved) {
				delete[] inf_bound;
				delete[] sup_bound;
				// the infeasibility is proved, the EmptyBox exception is raised
				throw PolytopeHullEmptyBoxException();
			}

			else if (stat == LPSolver::Status::Infeasible) {
				// the infeasibility is found but not proved, no other call is needed
				break;
			}

			else if (stat == LPSolver::Status::Unknown) {
				int next=-1;
				for (int j=0;j<nb_var;j++) {
					if (inf_bound[j]==0) {
						nexti=j;  next=0;  infnexti=0;
						break;
					}
					else if  (sup_bound[j]==0) {
						nexti=j;  next=0;  infnexti=1;
						break;
					}
				}
				if (next==-1)  break;
			}

		}
		else if (infnexti==1 && sup_bound[i]==0) { // computing the right bound :  maximizing x_i
			sup_bound[i]=1;
			mylinearsolver.set_cost(i, -1.0);
			stat= mylinearsolver.minimize();
			mylinearsolver.set_cost(i, 0.0);
			//cout << "[polytope-hull]->[optimize] simplex for right bound returns stat=" << stat << endl;
			if( stat == LPSolver::Status::OptimalProved) {
				opt = -mylinearsolver.minimum();
				//std::cout << "opt=" << opt << endl;
				if(opt.ub() <box[i].lb()) {
					delete[] inf_bound;
					delete[] sup_bound;
					throw PolytopeHullEmptyBoxException();
				}

				primal_sols[2*i+1]=mylinearsolver.not_proved_primal_sol();
				primal_sol_found.add(2*i+1);

				if (opt.ub() < box[i].ub()) {
					Vector dual_vector = mylinearsolver.not_proved_dual_sol();
					P.resize(P.nb_rows()+1,dual_vector.size()-box.size());
					for (int i = box.size() ; i < dual_vector.size() ; i++){
						P[P.nb_rows()-1][i-box.size()] = -dual_vector[i];
					}
					box[i] =Interval( box[i].lb(), opt.ub());
					mylinearsolver.set_bounds(i,box[i]);
				}

				if (!choose_next_variable(box,nexti,infnexti, inf_bound, sup_bound)) {
					break;
				}
			}
			else if(stat == LPSolver::Status::InfeasibleProved) {
				delete[] inf_bound;
				delete[] sup_bound;
				// the infeasibility is proved,  the EmptyBox exception is raised
				throw PolytopeHullEmptyBoxException();
			}
			else if (stat == LPSolver::Status::Infeasible) {
				// the infeasibility is found but not proved, no other call is needed
				break;
			}

			else if (stat == LPSolver::Status::Unknown) {
				int next=-1;
				for (int j=0;j<nb_var;j++) {
					if (inf_bound[j]==0) {
						nexti=j;  next=0;  infnexti=0;
						break;
					}
					else if (sup_bound[j]==0) {
						nexti=j;  next=0;  infnexti=1;
						break;
					}
				}
				if (next==-1) break;
			}
		}
		else break; // in case of stat==MAX_ITER  we do not recall the simplex on a another variable  (for efficiency reason)
	}


	delete[] inf_bound;
	delete[] sup_bound;
}

bool CtcPolytopeHull::choose_next_variable(IntervalVector & box, int & nexti, int & infnexti, int* inf_bound, int* sup_bound) {

	bool found = false;
	// the primal solution : used by choose_next_variable
	Vector primal_solution = mylinearsolver.not_proved_primal_sol();
	//cout << " primal " << primal_solution << endl;

	// The Achterberg heuristic for choosing the next variable (nexti) and its bound (infnexti) to be contracted (cf Baharev paper)
	// and updating the indicators if a bound has been found feasible (with the precision prec_bound)
	// called only when a primal solution is found by the LP solver (use of primal_solution)

	// double prec_bound = mylinearsolver.getEpsilon(); // relative precision for the indicators TODO change with the precision of the optimizer ??
	double prec_bound = 1.e-8; // relative precision for the indicators      :  compatibility for testing  BNE
	double delta=1.e100;
	double deltaj=delta;

	for (int j=0; j<nb_var; j++)	{

		if (inf_bound[j]==0) {
			deltaj= fabs(primal_solution[j]- box[j].lb());
			if ((fabs (box[j].lb()) < 1 && deltaj < prec_bound) ||
					(fabs (box[j].lb()) >= 1 && fabs (deltaj /(box[j].lb())) < prec_bound))	{
				inf_bound[j]=1;
			}
			if (inf_bound[j]==0 && deltaj < delta) 	{
				nexti=j; infnexti=0;delta=deltaj; found =true;
			}
		}

		if (sup_bound[j]==0) {
			deltaj = fabs (primal_solution[j]- box[j].ub());


			if ((fabs (box[j].ub()) < 1 && deltaj < prec_bound) 	||
					(fabs (box[j].ub()) >= 1 && fabs (deltaj/(box[j].ub())) < prec_bound)) {
				sup_bound[j]=1;
			}
			if (sup_bound[j]==0 && deltaj < delta) {
				nexti=j; infnexti=1;delta=deltaj;  found =true;
			}

		}


	}
	return found;
}

} // end namespace ibex
