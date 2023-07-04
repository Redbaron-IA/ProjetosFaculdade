def move_zeros(nums):

    sentinela = 0

    for i, num in enumerate(nums):
        if num != 0:
            nums[sentinela], nums[i] = nums[i], nums[sentinela]
            sentinela += 1

        print("Interação " + str(i) + ": Linta de entrada: " + str(nums))
        
    return nums

print("Lista final: ", move_zeros([0, 1, 0, 3, 12]))