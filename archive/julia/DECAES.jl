#=
DECAES function for Julia
B. Prigent
v 1, 05-Jun-2023
=#
import Pkg

tempdir = mktempdir()
Pkg.activate(tempdir)
Pkg.add(["ArgParse", "Pope"])

using ArgParse, Pope
Pope.dostuff()



; julia --project=@decaes -e 'import Pkg; Pkg.add("DECAES"); Pkg.build("DECAES")'
decaes "C:\Users\bprigent\MyDatas\TestFolder\C2PI\C2PI.nii.gz" --T2map --T2part --TE 7e-3 --nT2 40 --T2Range 7e-3 2.0 --SPWin 7e-3 25e-3 --MPWin 25e-3 200e-3 --Reg lcurve --output "C:\Users\bprigent\MyDatas\TestFolder\ResultsTest\"
