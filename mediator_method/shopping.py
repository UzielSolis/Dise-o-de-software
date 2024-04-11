class shop:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.productos = []
        self.app = None

    def agregar_producto(self, cantidad, producto):
        for n in range(cantidad):
            self.productos.append(producto)
        print(f"[{self.nombre}] Producto agregado: {cantidad} {producto}")

    def recibir_compra(self, compra):
        for n in range(len(self.productos)):
            if compra == self.productos[n]:
                self.productos.pop(n)
                print(f"Compra recibida: {compra}")
                break


class user:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.carrito = []
        self.app = None

    def agregar_carrito(self, producto):
        self.carrito.append(producto)

    def comprar(self):
        self.carrito.clear()


class app:
    def __init__(self) -> None:
        self.tiendas = []
        self.usuarios = []

    def agregar_tienda(self, tienda: shop):
        self.tiendas.append(tienda)
        tienda.app = self

    def agregar_usuario(self, usuario: user):
        self.usuarios.append(usuario)
        usuario.app = self

    def comprar(self, usuario: user, carrito):
        usuario.comprar()
        print(f"Compra realizada: {carrito}")

    def hacer_compra(self, usuario: user, shop: shop, compra):
        print(f"[{usuario.nombre}] comprando en {shop.nombre}")
        for n in range(len(usuario.carrito)):
            shop.recibir_compra(compra)
            self.comprar(usuario, usuario.carrito[n])

    def agregar_carrito(self, usuario: user, producto):
        usuario.agregar_carrito(producto)

    def agregar_producto(self, cantidad: int, tienda: shop, producto):
        tienda.agregar_producto(cantidad, producto)


if __name__ == "__main__":
    app = app()
    tienda = shop("Tienda 1")
    usuario = user("Usuario 1")
    app.agregar_tienda(tienda)
    app.agregar_usuario(usuario)
    app.agregar_producto(1, tienda, "manzanas")
    app.agregar_carrito(usuario, "Producto 1")
    app.hacer_compra(usuario, tienda, usuario.carrito)

    tienda_2 = shop("Tienda 2")
    app.agregar_tienda(tienda_2)
    app.agregar_producto(5, tienda_2, "manzanas")
