#HARRIS HAWK OPTIMIZATION ON DIGITAL CIRCUITS

Optimize a full adder circuit for static leakage and transmission delays using the Harris Hawk Optimisation algorithm

Folder structure in submission
	
	Report.pdf 			-	The final Report with all the procedure, outputs and observations
	Presentation.pdf 	-	The presentation with updated results and graphs
	src 				-	contains all the codes and required .sp,.mgk files
		optz.py 			-	Code for combining the hspice and HHO  
		HHO.py 			-	Python implementation of Harris Hawk optimization
		.sp_files 		-	The parameters specification files

Folder structure on server
	Similar to the original structure except that the path is different:
	PATH = "/home/DVD7_algo/final/final_runs/0/"	 

Commands to run:
	1) python optz.py 	-	generates final_params.txt (a pickle file to store best parameters)
	2) python plot.py 	-	generates test.png(using the above generated pickle file), a plot of the optimal curve similar to pareto 

	Note : Change the values of the temperature,thickness etc in the "fa_leak_25,0.8.sp" , "fa_del_25,0.8.sp" and  "22nm_MGK.pm" files as per your requirements and then run the codes.

Process:
	The optz file generates params.txt having the best optimal values(skyline parameters)
	The plot.py uses these parameters, runs hspice with each of those parameters and plots delays Vs leakages graph