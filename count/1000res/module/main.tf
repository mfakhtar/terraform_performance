module "null" { 
    source = "./null_module"
    count = 1000
}

/*
terraform apply --auto-approve  0.17s user 0.07s system 43% cpu 0.549 total
terraform apply --auto-approve  0.66s user 0.21s system 88% cpu 0.974 total
terraform apply --auto-approve  13.43s user 1.78s system 135% cpu 11.230 total
terraform apply --auto-approve  0.19s user 0.07s system 59% cpu 0.434 total
terraform apply --auto-approve  0.68s user 0.20s system 110% cpu 0.792 total
terraform apply --auto-approve  13.43s user 1.78s system 135% cpu 11.230 total
*/

#terraform apply --auto-approve  13.55s user 1.80s system 134% cpu 11.432 total
#terraform apply --auto-approve  13.99s user 1.75s system 138% cpu 11.381 total
#terraform apply --auto-approve  23.32s user 2.17s system 160% cpu 15.838 total
