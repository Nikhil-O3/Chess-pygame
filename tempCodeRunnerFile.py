
        # Header
        print("\n    0  1  2  3  4  5  6  7")
        print("  ──────────────────────────")
        
        for rank in range(0,8):
            row = self.board[rank]
            print(f"{rank} │", end=" ")
            for square in row:
                glyph = self.symb.get(square, '_')
                print(glyph, end="  ")
            print(f"│ {8 - rank}")
        
        # Footer
        print("  ──────────────────────────")
        print("    a  b  c  d  e  f  g  h\n")
