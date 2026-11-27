# Temporary resource augmentation | الإضافة المؤقتة ثم الإرجاع

A short cross-domain method note, separate from the berth-allocation model and from Pascal/Singmaster or polygon research. It formalizes the owner's seven-camels example as an exact conservation calculation; it is not a novelty claim or an empirical result.

## R01 question

When can a temporary whole unit be added to an indivisible allocation, used to make fractional shares integral, and then returned without changing the original total?

## Result

If M is the original total, r_i are the stated shares of the augmented total, and q=sum(r_i), exact return of a temporary amount b requires

    q(M+b)=M
    b=M(1-q)/q

For a positive original total, a positive returned addition requires 0<q<1. For indivisible units, b must be a nonnegative integer and every r_i(M+b) must be an integer. These conditions are necessary and sufficient for the stated proportional allocations to sum to M and leave exactly b units to return.

## Seven-camels instance

Interpret the shares as: first receives half the total; second half of the first share; third half of the second share. Their shares of the same total are 1/2, 1/4, and 1/8. Thus q=7/8. With M=7:

    b = 7(1-7/8)/(7/8) = 1
    augmented total = 8
    allocations = 4, 2, 1
    allocated total = 7; residual = 1

The temporary camel can be returned because the exact leftover equals the added unit. The proof is conservation plus the integer check; the script reproduces the arithmetic with exact fractions.

## Shared pattern and differences

The transferable sequence is: identify a temporary resource; add it; perform the operation; verify the conserved quantity and exact residual; remove the temporary resource only after the invariant holds.

This resembles using an empty scratch variable or cup as temporary workspace. It is structurally related to, but physically different from, the ship holding buffer in R06–R07: in the camel example, the temporary unit is an arithmetic aid and is returned immediately; a berth holding place is real capacity occupied over time and may fill, causing upstream blocking. The puzzle does not justify assuming that a real process has spare capacity.

## Limits and status

This is an elementary exact identity and a user-provided illustration. No originality, new allocation algorithm, physical-resource model, or universal operational rule is claimed. See [probe.py](probe.py) and [captured output](probe.log).
