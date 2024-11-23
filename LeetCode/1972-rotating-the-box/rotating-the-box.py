class Solution:
    def rotate(self, box):
        """
        Rotates an n x m 2D matrix representing an 
        image by 90 degrees clockwise.
        Args:
            matrix: A list of lists representing the image.
        Returns:
            A list of lists representing the rotated image.
        """
        n = len(box)
        m = len(box[0])
        # Transpose the matrix
        transposed_matrix = [[box[j][i] for j in range(n)] for i in range(m)]
        # Reverse each row
        rotated_matrix = [[row[i] for i in range(n - 1, -1, -1)] for row in transposed_matrix]
        return rotated_matrix
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rotated_box = self.rotate(box)
        rows, cols = len(rotated_box), len(rotated_box[0])

        for c in range(cols):
            free_r = -1
            for r in range(rows - 1, -1, -1):
                if rotated_box[r][c] == '.':
                    if free_r == -1:
                        free_r = r
                elif rotated_box[r][c] == '*':
                    free_r = -1
                else:
                    if free_r != -1:
                        rotated_box[free_r][c] = '#'
                        rotated_box[r][c] = '.'
                        while free_r >= r and rotated_box[free_r][c] != '.':
                            free_r -= 1
        return rotated_box
        