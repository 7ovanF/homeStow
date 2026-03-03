.data
    nama: .space 11
    promptNama: .asciiz "Siapakah nama Anda? "
    promptNomor: .asciiz "\nNomor antrian: "

    outputNama: .asciiz "\nSelamat datang, "
    outputNomorP1: .asciiz "\nAntrian kakak nomor "
    outputNomorP2: .asciiz ". Mohon ditunggu pesanannya!"

.text
.globl main
main:

    # === minta input nama ===
    # print prompt
    li $v0, 4 # 4: service code print string
    la $a0, promptNama # load address string prompt nama
    syscall
    
    # minta input string
    li $v0, 8 # 8: service code input string
    li $a1, 11 # maks karakter 10, load ke argumen
    la $a0, nama # load address memori "nama" ke argumen
    syscall
     
    # === minta input nomor ===
    # print prompt
    li $v0, 4 # 4: service code print string
    la $a0, promptNomor # load address string prompt nomor
    syscall
    
    li $v0, 5 # 5: service code input integer
    syscall
    add $t0, $v0, $zero # move dari $v0 (tempat input disimpan) ke temporary
   
    # === print output ===
    # = Print Nama =
    li $v0, 4 # 4: service code print string
    la $a0, outputNama # load address sapaan
    syscall
    
    li $v0, 4 # 4: service code print string
    la $a0, nama # load address nama yang diinput
    syscall

    # = Print Nomor Antrian =
    li $v0, 4 # 4: service code print string
    la $a0, outputNomorP1 # load address output nomor (part 1)
    syscall
    
    li $v0, 1 # 1: service code print integer
    add $a0, $t0, $zero # move isi $t0 (inputan) ke argumen
    syscall
    
    li $v0, 4 # 4: service code print string
    la $a0, outputNomorP2 # load address output nomor (part 2)
    syscall
    
    # === exit ===
    li $v0, 10 # 10: service code exit
    syscall