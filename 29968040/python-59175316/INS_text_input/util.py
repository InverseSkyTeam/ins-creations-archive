import pygame


def surface_concatenate(a: pygame.Surface, b: pygame.Surface):
    a_w, a_h = a.get_size()
    b_w, b_h = b.get_size()

    res = pygame.Surface((a_w + b_w, max(a_h, b_h)), pygame.SRCALPHA)
    res.blit(a, a.get_rect(midleft=res.get_rect().midleft))
    res.blit(b, b.get_rect(midright=res.get_rect().midright))

    return res.convert_alpha()


def draw_shadow(w, h):
    surface = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(surface, (0, 0, 0), (0, 0, w, h), border_radius=10)
    surface.set_alpha(70)
    return surface


def mod_equal(mod, target_mod):
    if mod == target_mod == pygame.KMOD_NONE:
        return True
    return mod & target_mod
