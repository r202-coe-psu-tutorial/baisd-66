def get_staircase(base: int, display: str) -> str:
    data = []
    for i in range(1, base + 1):
        data.append(f"{display*i:>{base}}")

    return "\n".join(data)


if __name__ == "__main__":
    print(get_staircase(4, "#"))
