from django.db import models


class Pais(models.Model):
    _id = models.AutoField(db_column='PaisId', primary_key=True)
    nome = models.CharField(db_column='PaisNome', max_length=50, blank=True, null=True)
    sigla = models.CharField(db_column='PaisSigla', max_length=50, blank=True, null=True)
    exibicao = models.TextField(db_column='PaisExibicao', blank=True, null=True)

    def __str__(self):
        return '{id} - {sigla} - {nome}'.format(id=self._id, sigla=self.sigla, nome=self.nome)

    class Meta:
        managed = False
        db_table = 'Pais'
        verbose_name_plural = 'Paises'


class Estado(models.Model):
    _id = models.AutoField(db_column='EstadoId', primary_key=True)
    nome = models.CharField(db_column='EstadoNome', max_length=50, blank=True, null=True)
    sigla = models.CharField(db_column='EstadoSigla', max_length=50, blank=True, null=True)
    pais = models.ForeignKey(Pais, db_column='PaisId', blank=True, null=True)
    exibicao = models.TextField(db_column='EstadoExibicao', blank=True, null=True)

    def __str__(self):
        return '{id} - {sigla} - {nome} ({pais})'.format(id=self._id,
                                                         sigla=self.sigla,
                                                         nome=self.nome,
                                                         pais=self.pais.nome)

    class Meta:
        managed = False
        db_table = 'Estado'


class Cidade(models.Model):
    _id = models.AutoField(db_column='CidadeId', primary_key=True)
    nome = models.CharField(db_column='CidadeNome', max_length=50, blank=True, null=True)
    estado = models.ForeignKey(Estado, db_column='EstadoId', blank=True, null=True)
    exibicao = models.TextField(db_column='CidadeExibicao', blank=True, null=True)

    def __str__(self):
        return '{id} - {nome} - {estado} ({pais})'.format(id=self._id,
                                                          nome=self.nome,
                                                          estado=self.estado.sigla,
                                                          pais=self.estado.pais.sigla)

    class Meta:
        managed = False
        db_table = 'Cidade'


class Bairro(models.Model):
    _id = models.AutoField(db_column='BairroId', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='BairroNome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endereco = models.TextField(db_column='BairroEndereco', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='BairroCEP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='BairroNumero', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='BairroComplemento', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    status = models.CharField(db_column='BairroStatus', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    cidade = models.ForeignKey(Cidade, db_column='CidadeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bairro'

    def __str__(self):
        return '{id} - {nome} - {estado} ({pais})'.format(id=self._id,
                                                          nome=self.nome,
                                                          estado=self.estado.sigla,
                                                          pais=self.estado.pais.sigla)


class Classe(models.Model):
    _id = models.AutoField(db_column='ClasseId', primary_key=True)
    nome = models.CharField(db_column='ClasseNome', max_length=50, blank=True, null=True)

    def __str__(self):
        return '{id} - {nome}'.format(id=self._id,
                                      nome=self.nome)

    class Meta:
        managed = False
        db_table = 'Classe'


class Segmento(models.Model):
    _id = models.AutoField(db_column='SegmentoId', primary_key=True)
    nome = models.CharField(db_column='SegmentoNome', max_length=50, blank=True, null=True)
    classe = models.ForeignKey(Classe, db_column='SegmentoClasse', blank=True, null=True)

    def __str__(self):
        return '{id} - {nome} ({classe})'.format(id=self._id,
                                                 nome=self.nome,
                                                 classe=self.classe.nome)

    class Meta:
        managed = False
        db_table = 'Segmento'


class Location(models.Model):
    _id = models.AutoField(db_column='LocationId', primary_key=True)
    nome = models.CharField(db_column='LocationNome', max_length=50, blank=True, null=True)
    descricao = models.TextField(db_column='LocationDescricao', blank=True, null=True)
    icon = models.TextField(db_column='LocationIcon', blank=True, null=True)
    latitude = models.CharField(db_column='LocationLatitude', max_length=50, blank=True, null=True)
    longitude = models.CharField(db_column='LocationLongitude', max_length=50, blank=True, null=True)
    segmento = models.ForeignKey(Segmento, db_column='SegmentoId', max_length=50, blank=True, null=True)

    def __str__(self):
        return '{id} - {nome} ({latitude}, {longitude})'.format(id=self._id,
                                                                nome=self.nome,
                                                                latitude=self.latitude,
                                                                longitude=self.longitude)

    class Meta:
        managed = False
        db_table = 'Location'
        verbose_name_plural = 'Locations'


class Fornecedor(models.Model):
    _id = models.AutoField(db_column='FornecedorId', primary_key=True)
    segmento = models.ForeignKey(Segmento, db_column='FornecedorSegmento', max_length=50, blank=True, null=True)
    nome = models.CharField(db_column='FornecedorNome', max_length=50, blank=True, null=True)
    descricao = models.TextField(db_column='FornecedorDescricao', blank=True, null=True)
    precomedio = models.DecimalField(db_column='FornecedorPrecoMedio', max_digits=19, decimal_places=4, blank=True,
                                     null=True)
    cidade = models.ForeignKey(Cidade, db_column='FornecedorCidade', max_length=50, blank=True, null=True)
    telefone1 = models.DecimalField(db_column='FornecedorTelefone01', max_digits=18, decimal_places=0, blank=True,
                                    null=True)
    telefone2 = models.DecimalField(db_column='FornecedorTelefone02', max_digits=18, decimal_places=0, blank=True,
                                    null=True)
    cnpj = models.CharField(db_column='FornecedorCNPJ', max_length=50, blank=True, null=True)

    def __str__(self):
        return '{id} - {nome} ({cnpj})'.format(id=self._id,
                                               nome=self.nome,
                                               cnpj=self.cnpj)

    class Meta:
        managed = False
        db_table = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Item(models.Model):
    _id = models.AutoField(db_column='ItemId', primary_key=True)
    produto = models.CharField(db_column='ItemProduto', max_length=50, blank=True, null=True)
    descricao = models.TextField(db_column='ItemDescricao', blank=True, null=True)
    valor_unitario = models.DecimalField(db_column='ItemValorUnitario', max_digits=19, decimal_places=4, blank=True,
                                         null=True)
    fornecedor = models.ForeignKey(Fornecedor, db_column='ItemFornecedor', max_length=50, blank=True, null=True)
    data_vigencia = models.CharField(db_column='ItemDataVigencia', max_length=10, blank=True, null=True)
    hora_vigencia = models.CharField(db_column='ItemHoraVigencia', max_length=10, blank=True, null=True)

    def __str__(self):
        return '{id} - {produto} ({valor_unitario}) - {fornecedor}'.format(id=self._id,
                                                                           produto=self.produto,
                                                                           valor_unitario=self.valor_unitario,
                                                                           fornecedor=self.fornecedor.nome)

    class Meta:
        managed = False
        db_table = 'Item'
        verbose_name_plural = 'Itens'


class UsuarioFacebook(models.Model):
    _id = models.AutoField(db_column='FaceId', primary_key=True)
    facebook_id = models.TextField(db_column='FacebookId', blank=True, null=True)
    nome = models.CharField(db_column='FacebookNome', max_length=50, blank=True, null=True)
    email = models.CharField(db_column='FacebookEmail', max_length=50, blank=True, null=True)
    datra_first_login = models.CharField(db_column='FacebookFirstLogin', max_length=50, blank=True, null=True)
    data_last_login = models.CharField(db_column='FacebookLastLogin', max_length=50, blank=True, null=True)
    newsletter = models.NullBooleanField(db_column='FacebookNewsLetter')
    is_adm = models.NullBooleanField(db_column='FacebookADM')

    class Meta:
        managed = False
        db_table = 'UsuarioFacebook'


class Usuario(models.Model):
    _id = models.IntegerField(db_column='UsuarioId', primary_key=True)
    email = models.CharField(db_column='UsuarioEmail', max_length=50, blank=True, null=True)
    senha = models.CharField(db_column='UsuarioSenha', max_length=50, blank=True, null=True)
    ativo = models.NullBooleanField(db_column='UsuarioAtivo')
    is_conta_validada = models.NullBooleanField(db_column='UsuarioContaValidada')
    is_fornecedor = models.NullBooleanField(db_column='UsuarioFornecedor')
    is_adm = models.NullBooleanField(db_column='UsuarioADM')
    nascimento = models.CharField(db_column='UsuarioNascimento', max_length=50, blank=True, null=True)
    pais = models.CharField(db_column='UsuarioPais', max_length=50, blank=True, null=True)
    cidade = models.CharField(db_column='UsuarioCidade', max_length=50, blank=True, null=True)
    linguagem = models.CharField(db_column='UsuarioLinguagem', max_length=50, blank=True, null=True)
    data_criacao = models.CharField(db_column='UsuarioCriacao', max_length=50, blank=True, null=True)
    data_last_login = models.CharField(db_column='UsuarioLastLogin', max_length=50, blank=True, null=True)
    newsletter = models.NullBooleanField(db_column='UsuarioNewsLetter')
    is_facebook = models.NullBooleanField(db_column='UsuarioFacebook')
    facebook = models.ForeignKey(UsuarioFacebook, db_column='IdFacebook', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuario'


class Token(models.Model):
    _id = models.AutoField(db_column='TokenId', primary_key=True)
    usuario = models.ForeignKey(Usuario, db_column='UsuarioId', blank=True, null=True)
    nome = models.CharField(db_column='TokenNome', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Token'
