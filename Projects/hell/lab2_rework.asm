.data
str_prompt_truk: .asciiz "Masukkan cuan per truk (dalam juta) (do NOT input more than 42 times): "

str_truk: .asciiz "Truk: Rp. "
str_juta: .asciiz " Juta -> "
str_cuan: .asciiz "CUAN\n"
str_t_cuan: .asciiz "TIDAK CUAN\n"

str_separator: .asciiz "--------------------\n"
str_total_cuan: .asciiz "Total Cuan: "
str_total_t_cuan: .asciiz "\nTotal Tidak Cuan: "
str_tercuan: .asciiz "\nTERCUAN: "
str_tercuan_juta: .asciiz " juta"

.align 2 # alignment fawked because of asciizes
array: .space 168 # 42 words reserved

# TODO: learn shifts

.text
.globl main
main:
    # standards!!!
    # $t0 = boolean
    # $t1 = array
    la $t1, array
    # $t2-4 = total cuan, total tidak cuan, pendapatan tertinggi
    # $t5 = treshold 19jt
    addi $t5, $zero, 19
    # i didnt consider this!
    # $t7 = current iterated element (maybe this should be, like, $t2 since it's pretty common
    
    # idea: t0 definitely boolean, t1 array if exists, followed by stored data, finally tresholds, then impromptu things after
    # idk what exactly $sN registers are for... theyre preserved across function calls, but function calls arent used yet
    
    # ===== LOOP STORE TO ARRAY =====
    inputLoop:
        # print prompt
        addi $v0, $zero, 4
        la $a0, str_prompt_truk
        syscall
        
        # receive input
        addi $v0, $zero, 5
        syscall
        add $t7, $v0, $zero # move input to $t7
        
        # insert data to array (even when zero)
        sw $t7, 0($t1)
        # increment address by 4 for next write
        addi $t1, $t1, 4
        
        # if input=0: end
        bne $t7, $zero, inputLoop
    
    # ===== LOOP ANALYZE EACH =====
    la $t1, array # reset array reader position
    analyzeLoop:
        # load current read array element
        lw $t7, 0($t1)

        # if 0: end loop, summarize
        beq $t7, $zero, summary
        
        # if not, show data
    	addi $v0, $zero, 4
    	la $a0, str_truk
    	syscall
    	
    	addi $v0, $zero, 1 # print integer
    	add $a0, $t7, $zero
    	syscall
    	
    	addi $v0, $zero, 4
    	la $a0, str_juta
    	syscall
    	
    	# check if value < 19, if yes (1) branch to not poggers
    	slt $t0, $t7, $t5
    	bne $t0, $zero, tidakCuan
    	
    	cuan:
    	    addi $v0, $zero, 4
    	    la $a0, str_cuan
    	    syscall
    	    
    	    addi $t2, $t2, 1 # cuan count + 1
    	    
    	    j continueAnalyze
    	    
    	tidakCuan:
    	    addi $v0, $zero, 4
    	    la $a0, str_t_cuan
    	    syscall
    	    
    	    addi $t3, $t3, 1 # tidak cuan count + 1
    	    
    	    j continueAnalyze
    	    
    	continueAnalyze:
    	
    	# if max is smaller than current, set new max
    	slt $t0, $t4, $t7
    	beq $t0, $zero, skipSetMax
    	add $t4, $t7, $zero
    	skipSetMax:
    	
        # increment by 4; go to next word
        addi $t1, $t1, 4
        j analyzeLoop
    
    # ===== SUMMARY =====
    summary:
        # Print separator
        addi $v0, $zero, 4
        la $a0, str_separator
        syscall
        
        # Print total cuan
        addi $v0, $zero, 4
        la $a0, str_total_cuan
        syscall
        
        addi $v0, $zero, 1
        add $a0, $t2, $zero
        syscall
        
        # Print total tidak cuan
        addi $v0, $zero, 4
        la $a0, str_total_t_cuan
        syscall
        
        addi $v0 $zero, 1
        add $a0, $t3, $zero
        syscall
    
        # Print tercuan
        addi $v0, $zero, 4
        la $a0, str_tercuan
        syscall
        
        addi $v0, $zero, 1
        add $a0, $t4, $zero
        syscall
        
        addi $v0, $zero, 4
        la $a0, str_tercuan_juta
        syscall
        
    # ===== Exit =====
    exit:
        addi $v0, $zero, 10
        syscall