# Resource acquisition is initialization (RAII) is a programming idiom
# used in several object-oriented, statically typed programming languages
# to describe a particular language behavior.
# In RAII, holding a resource is a class invariant,
# and is tied to object lifetime.

def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    fd1 = "classified_data.txt"
    fd2 = "security_protocols.txt"
    our_str = "[CLASSIFIED] New security protocols archived"
    print("Initiating secure vault access...")
    with open(fd1) as file1:
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")
        print(file1.read())
    file1.close()
    with open(fd2, "w") as file2:
        print("\nSECURE PRESERVATION:")
        file2.write(our_str)
        print(our_str)
    file2.close()
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
