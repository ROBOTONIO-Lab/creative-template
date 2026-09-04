import asyncio
import pygame  # noqa: F401 — ΜΗΝ το σβήσεις: το pygbag διαβάζει ΜΟΝΟ αυτό το αρχείο για imports

# ---------------- Ρυθμίσεις ----------------
WIDTH, HEIGHT = 800, 600     # μέγεθος παραθύρου
FPS = 60                     # καρέ ανά δευτερόλεπτο


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Το παιχνίδι μου")
    clock = pygame.time.Clock()

    # ---------- ΕΔΩ φτιάχνεις τα πράγματα του παιχνιδιού σου ----------
    # (τον παίκτη, το σκορ, ...)

    running = True
    while running:
        # 1) ΓΕΓΟΝΟΤΑ — τι έκανε ο χρήστης;
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2) ΛΟΓΙΚΗ — τι αλλάζει σε αυτό το καρέ;

        # 3) ΖΩΓΡΑΦΙΚΗ — σβήσε και ξαναζωγράφισε
        screen.fill((15, 40, 60))

        pygame.display.flip()

        clock.tick(FPS)
        await asyncio.sleep(0)  # ΜΗΝ το σβήσεις: χωρίς αυτό δεν τρέχει στο web

    pygame.quit()


asyncio.run(main())
