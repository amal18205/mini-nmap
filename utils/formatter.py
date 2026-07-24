def print_results(results):

    print("\n----------------------")
    print("Scan Results")
    print("----------------------\n")

    print(f"{'PORT':<10}{'STATE':<10}{'BANNER'}")

    for result in results:

        print(
            f"{result['port']:<10}"
            f"{result['state']:<10}"
            f"{result['banner']}"
        )

    print("\n----------------------")
