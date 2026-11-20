import itertools

# 1. Core Algorithms for Set Operations
def set_union(set_a, set_b):
    """Computes the union of two sets without just relying on shortcuts."""
    result = set(set_a)
    for item in set_b:
        if item not in result:
            result.add(item)
    return result

def set_intersection(set_a, set_b):
    """Computes the intersection of two sets."""
    result = set()
    for item in set_a:
        if item in set_b:
            result.add(item)
    return result

# 2. Truth Table Generator for Propositional Logic
def generate_truth_table():
    print("--- PROPOSITIONAL LOGIC TRUTH TABLE ---")
    print(f"{'P':<6} | {'Q':<6} | {'P AND Q':<8} | {'P OR Q':<8} | {'NOT P':<6} | {'P -> Q':<8}")
    print("-" * 55)
    
    # Generate all combinations of True/False for 2 variables
    for p, q in itertools.product([True, False], repeat=2):
        p_and_q = p and q
        p_or_q = p or q
        not_p = not p
        p_implies_q = (not p) or q  # Logical implication
        
        print(f"{str(p):<6} | {str(q):<6} | {str(p_and_q):<8} | {str(p_or_q):<8} | {str(not_p):<6} | {str(p_implies_q):<8}")
    print("\n")

# 3. Testing Input Parameters & 4. Validating Against Manual Calculations
def validate_operations():
    print("--- SET THEORY VALIDATION ---")
    # Test Case 1: Standard Sets
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    
    expected_union = {1, 2, 3, 4, 5, 6}       # Manual calculation
    expected_intersection = {3, 4}          # Manual calculation
    
    actual_union = set_union(A, B)
    actual_intersection = set_intersection(A, B)
    
    assert actual_union == expected_union, f"Union failed: got {actual_union}"
    assert actual_intersection == expected_intersection, f"Intersection failed: got {actual_intersection}"
    print(f"Test 1 Passed! Union: {actual_union}, Intersection: {actual_intersection}")

    # Test Case 2: Edge Case (Empty Set)
    C = set()
    D = {10, 20}
    assert set_union(C, D) == {10, 20}
    assert set_intersection(C, D) == set()
    print("Test 2 (Empty Set) Passed!")

if __name__ == "__main__":
    generate_truth_table()
    validate_operations()
