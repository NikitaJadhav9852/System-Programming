%macro Occurences 2
	mov eax,%1	
	xor ecx,ecx

%%lp:
	mov al,byte[eax]
	cmp al,byte[%2]
	je %%ans1
	cmp al,0
	je %%end
	inc eax
	jmp %%lp

%%ans1:
	push res1
	call printf
	add esp,4
	ret
%%end:
	push res2
	call printf
	add esp,4	
%endmacro

%macro Occus 3
	mov eax,%1	
	xor ecx,ecx

%%lp:
	mov al,byte[eax]
	cmp al,byte[%2]
	je %%ans1
	cmp al,0
	je %%end
	inc eax
	jmp %%lp
%endmacro
	
section  .data
	str1 db "Nikita",10,0
	str2 db "i",10,0
	res1 db "String is Present",10,0
	res2 db "String is Not Present",10,0

section .text
	global main
	extern printf

main:
	Occurences str1,str2
	Occurences str1,str2
