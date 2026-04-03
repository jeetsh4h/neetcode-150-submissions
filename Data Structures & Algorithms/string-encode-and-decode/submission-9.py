class Solution:
    MAGIC_KEY = "63f4945d921d599f27ae4fdf5bada3f1"
    EMPTY_KEY = "a4200d769bb7cac190247b93d0cecb46"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.EMPTY_KEY

        return self.MAGIC_KEY.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.EMPTY_KEY:
            return []

        return list(s.split(self.MAGIC_KEY))