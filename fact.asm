section .data
	msg db 'the factorial number %d ',10,0
	n db 5

section .text
	global main
	extern printf

main:	
	mov eax,1
	mov ebx,dword[n]
	
lp:
	cmp ebx,1
	je abc
	mul ebx
	dec ebx
	jmp lp

abc:	
	 push eax
	push msg
	call printf
	add esp,8
