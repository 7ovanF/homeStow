.data
    nama: .space 11
    
    promptNama: .asciiz "Masukkan nama pembeli: "
    promptPembayaran: .asciiz "\nMasukkan saldo pembayaran: "

    outputSuksesNama: .asciiz "\nHore "
    outputSukses: .asciiz "\nTransaksimu BERHASIL! "
    outputGagalNama: .asciiz "\nYah "
    outputGagal: .asciiz "\nTransaksimu GAGAL. Saldo kurang."

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
     
    # === minta input pembayaran ===
    # print prompt
    li $v0, 4 # 4: service code print string
    la $a0, promptPembayaran # load address string prompt pembayaran
    syscall
    
    li $v0, 5 # 5: service code input integer
    syscall
    add $t0, $v0, $zero # move dari $v0 (tempat input disimpan) ke temporary
   
    # ===== CEK VALID =====
    # Jika saldo pembayaran >= 15000: SUKSES
    blt $t0, 15000, gagal
    
    sukses:
        # === print output ===
        # = Print Nama =
        li $v0, 4 # 4: service code print string
        la $a0, outputSuksesNama # load address HOREEE
        syscall
    
        li $v0, 4 # 4: service code print string
        la $a0, nama # load address nama yang diinput
        syscall

        # = Print Pesan =
        li $v0, 4 # 4: service code print string
        la $a0, outputSukses # load address output pesan sukses
        syscall
    
        j exit # skip gagal
    
    gagal:
    # === print output ===
        # = Print Nama =
        li $v0, 4 # 4: service code print string
        la $a0, outputGagalNama # load address yah....
        syscall
    
        li $v0, 4 # 4: service code print string
        la $a0, nama # load address nama yang diinput
        syscall

        # = Print Pesan =
        li $v0, 4 # 4: service code print string
        la $a0, outputGagal # load address output pesan gagal... hiks
        syscall
        
        j exit # ke exit, gausah tapi readability ajah
    
    exit:
        li $v0, 10 # 10: service code exit
        syscall