---
name: international-seo
description: "International Seo — Skill especializada para international seo"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# International Seo

Esta skill capacita o Claude a planejar, executar e otimizar estratégias de SEO para múltiplos países e idiomas, garantindo visibilidade global e relevância local.

---

## Keywords

*   Hreflang
*   ccTLDs (country code Top-Level Domains)
*   gTLDs (generic Top-Level Domains)
*   Subdomínios Internacionais
*   Subdiretórios Internacionais
*   Localização de Conteúdo
*   Geotargeting Google Search Console
*   Keyword Research Multilíngue
*   Link Building Localizado
*   Schema Markup Internacional
*   Tradução SEO
*   Estratégia de Domínio Internacional

---

## Quick Start

1.  Auditar a estrutura de domínio atual (ccTLD, gTLD+subdomínio/subdiretório) e sua adequação para expansão internacional.
2.  Mapear os mercados-alvo e idiomas primários com base em dados de demanda e concorrência.
3.  Implementar `hreflang` para o conteúdo existente que possui versões em diferentes idiomas ou regiões.
4.  Configurar o geotargeting no Google Search Console para domínios gTLD, direcionando subdiretórios ou subdomínios a países específicos.
5.  Realizar um Keyword Research aprofundado para um mercado-piloto, identificando termos de busca locais e suas intenções.

---

## Core Workflows

### Workflow 1: Estratégia de Segmentação Geográfica e Conteúdo Localizado

Este workflow detalha a construção de uma presença digital adaptada para mercados internacionais, desde a estrutura técnica até a criação de conteúdo culturalmente relevante.

1.  **Passo 1: Seleção da Estrutura de URL e Domínio:**
    *   **Ação:** Decidir a melhor abordagem entre ccTLDs (ex: `site.de`), subdomínios (ex: `de.site.com`), ou subdiretórios (ex: `site.com/de/`) para cada mercado.
    *   **Exemplo:** Para uma empresa de software B2B visando mercados na Alemanha e França, a opção por `site.de` e `site.fr` (ccTLDs) pode sinalizar maior compromisso e confiança local, apesar do maior custo de aquisição e manutenção. No entanto, para testar um novo mercado como a Polônia, um subdiretório `site.com/pl/` em um gTLD pode ser uma alternativa mais econômica e gerenciável inicialmente. A escolha impacta diretamente a percepção do usuário e os sinais de geotargeting para os motores de busca.
2.  **Passo 2: Keyword Research Multilíngue e Localizada:**
    *   **Ação:** Utilizar ferramentas como Ahrefs, Semrush ou Google Keyword Planner para identificar termos de busca específicos de cada idioma e região, incluindo gírias e variações contextuais.
    *   **Exemplo:** Para um produto como "software de CRM", um pesquisador no Brasil pode buscar por "melhor CRM para pequenas empresas", enquanto na Espanha a busca pode ser "programa CRM para pymes" (pequeñas y medianas empresas). Na Argentina, o termo "software de gestión de clientes" pode ser mais comum. É crucial identificar essas nuances para otimizar o conteúdo corretamente. Ferramentas como o "Keyword Gap" do Semrush permitem comparar o ranking de termos entre mercados.
3.  **Passo 3: Localização de Conteúdo vs. Tradução:**
    *   **Ação:** Adaptar o conteúdo não apenas linguisticamente, mas culturalmente, considerando moeda, unidades de medida, feriados, referências locais e tom de voz.
    *   **Exemplo:** Um artigo sobre "dicas para economizar energia em casa" nos EUA pode focar em aquecimento e isolamento. No Brasil, o mesmo artigo deveria abordar o uso eficiente de ar condicionado, ventiladores e chuveiros elétricos, além de mencionar programas de eficiência energética do governo brasileiro. Incluir exemplos de preços de eletrodomésticos em BRL, comparando com o consumo médio local.
4.  **Passo 4: Estratégia de Link Building Local:**
    *   **Ação:** Adquirir backlinks de domínios relevantes e com autoridade no mercado-alvo, priorizando fontes locais e temáticas.
    *   **Exemplo:** Para um e-commerce de vinhos português, buscar links de blogs de culinária portugueses, sites de turismo em Portugal ou associações de produtores de vinho locais (ex: Vinhos do Porto, Douro). Evitar links de diretórios genéricos ou sites que não possuem relevância geográfica ou temática com o mercado português. Analisar o perfil de backlink de concorrentes locais com ferramentas como Ahrefs ou Moz Link Explorer para identificar oportunidades.

### Workflow 2: Otimização Técnica para Múltiplos Idiomas/Regiões

Este workflow foca nas implementações técnicas cruciais para garantir que os motores de busca compreendam e exibam o conteúdo certo para o público certo.

1.  **Passo 1: Implementação Robusta de `hreflang`:**
    *   **Ação:** Indicar a relação entre páginas em diferentes idiomas ou regiões usando tags `hreflang` no `<head>` do HTML, no sitemap XML ou no cabeçalho HTTP.
    *   **Exemplo:** Para uma página de "serviços" que tem versões em português do Brasil, espanhol da Espanha e inglês dos EUA, o código no `<head>` de cada página deve incluir:
        ```html
        <link rel="alternate" hreflang="pt-BR" href="https://www.exemplo.com/br/servicos/" />
        <link rel="alternate" hreflang="es-ES" href="https://www.exemplo.com/es/servicios/" />
        <link rel="alternate" hreflang="en-US" href="https://www.exemplo.com/en/services/" />
        <link rel="alternate" hreflang="x-default" href="https://www.exemplo.com/en/services/" />
        ```
        O atributo `x-default` é essencial para indicar a página padrão para usuários sem um idioma/região específica.
2.  **Passo 2: Configuração de Geotargeting no Google Search Console:**
    *   **Ação:** Para domínios gTLD (ex: .com, .org), usar a ferramenta "Segmentação Internacional" no Google Search Console para associar subdiretórios ou subdomínios a países específicos.
    *   **Exemplo:** Se o site `www.exemplo.com` possui um subdiretório `/fr/` para a França, configurar no GSC que `www.exemplo.com/fr/` é destinado à França. **Importante:** Esta configuração não deve ser usada para ccTLDs, pois o próprio domínio já indica a região.
3.  **Passo 3: Otimização de Velocidade de Carregamento e Hosting Local:**
    *   **Ação:** Implementar CDNs (Content Delivery Networks) e garantir que os servidores de hospedagem estejam geograficamente próximos aos mercados-alvo para reduzir a latência.
    *   **Exemplo:** Um e-commerce com público no Chile, México e Colômbia deve utilizar uma CDN com pontos de presença (PoPs) em Santiago, Cidade do México e Bogotá. Isso garante que os ativos do site (imagens, CSS, JS) sejam carregados rapidamente para os usuários nesses países, impactando positivamente o Core Web Vitals e a experiência do usuário. Ferramentas como Cloudflare ou Akamai são soluções comuns.
4.  **Passo 4: Implementação de Schema Markup para Informações Locais:**
    *   **Ação:** Utilizar schema markup (JSON-LD) para fornecer aos motores de busca informações detalhadas sobre negócios locais, produtos e eventos, adaptadas a cada região.
    *   **Exemplo:** Para uma rede de hotéis, cada página de hotel em uma cidade específica (ex: "Hotel X em Roma") deve ter um `LocalBusiness` schema com `address`, `telephone`, `openingHours` e `geo` (latitude/longitude) específicos para a unidade de Roma, em italiano. A versão em inglês para o mesmo hotel teria o mesmo schema, mas adaptado para o idioma, mantendo os dados geográficos e de contato da filial de Roma.

---

## Templates

### Implementação `hreflang` em XML Sitemap

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://www.exemplo.com/br/solucoes-cloud</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="https://www.exemplo.com/br/solucoes-cloud" />
    <xhtml:link rel="alternate" hreflang="es-MX" href="https://www.exemplo.com/mx/soluciones-nube" />
    <xhtml:link rel="alternate" hreflang="en-US" href="https://www.exemplo.com/us/cloud-solutions" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.exemplo.com/us/cloud-solutions" />
  </url>
  <url>
    <loc>https://www.exemplo.com/mx/soluciones-nube</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="https://www.exemplo.com/br/solucoes-cloud" />
    <xhtml:link rel="alternate" hreflang="es-MX" href="https://www.exemplo.com/mx/soluciones-nube" />
    <xhtml:link rel="alternate" hreflang="en-US" href="https://www.exemplo.com/us/cloud-solutions" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.exemplo.com/us/cloud-solutions" />
  </url>
  <url>
    <loc>https://www.exemplo.com/us/cloud-solutions</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="https://www.exemplo.com/br/solucoes-cloud" />
    <xhtml:link rel="alternate" hreflang="es-MX" href="https://www.exemplo.com/mx/soluciones-nube" />
    <xhtml:link rel="alternate" hreflang="en-US" href="https://www.exemplo.com/us/cloud-solutions" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.exemplo.com/us/cloud-solutions" />
  </url>
  <!-- Incluir todas as URLs canônicas com suas respectivas alternativas -->
</urlset>
```

### Brief de Conteúdo Localizado (Exemplo: México)

```
**Título Sugerido:** "Los Mejores Tacos al Pastor en la Ciudad de México: Guía Definitiva 2024"

**Mercado Alvo:** México
**Idioma:** Espanhol (MX)
**Persona:** Moradores e turistas na Cidade do México, amantes de gastronomia, buscam autenticidade e qualidade em tacos.

**Keywords Primárias:**
- "Mejores tacos al pastor CDMX" (Volume: 2.5k, Dificuldade: Média)
- "Dónde comer tacos al pastor México" (Volume: 1.8k, Dificuldade: Baixa-Média)
- "Taco al pastor auténtico" (Volume: 1.0k, Dificuldade: Média)

**Keywords Secundárias/LSI:**
- "Taquerías recomendadas Ciudad de México"
- "Historia del taco al pastor"
- "Precios tacos CDMX"
- "Salsas para tacos al pastor"

**Estrutura de Conteúdo:**
1.  **Introdução:** A importância cultural e a ubiquidade do taco al pastor na CDMX.
2.  **O que torna um bom Taco al Pastor?** Ingredientes (carne marinada, piña, cebolla, cilantro), preparo (trompo), e o papel do taquero.
3.  **As 7 Melhores Taquerías na CDMX (com exemplos REAIS):**
    -   El Califa (Colonia Condesa): ambiente moderno, carne suculenta.
    -   El Vilsito (Narvarte Poniente): famosa por ser uma oficina mecânica de dia e taquería de noite.
    -   Los Cocuyos (Centro Histórico): tradição e sabor.
    -   Taquería Orinoco (Roma Norte): estilo Monterrey, tortillas de harina.
    -   Tacos Don Manolito (várias unidades): variedade e qualidade consistente.
    -   Taquería El Fogoncito (Polanco): ambiente familiar.
    -   Tacos Beto (Nápoles): destaque pelas salsas.
    (Para cada taquería: localização exata, horários, faixa de preço (MXN), o que pedir além do al pastor).
4.  **Dicas para Explorar a Cena de Tacos na CDMX:** Como pedir, gorjetas, acompanhamentos (limón, salsas).
5.  **Conclusão:** Convite para experimentar e compartilhar as próprias descobertas.

**Call to Action:** "Planeje sua rota de tacos e descubra a verdadeira essência gastronômica da Cidade do México!"

**Notas:**
-   Incluir mapa interativo com as taquerías mencionadas.
-   Usar pesos mexicanos (MXN) para preços.
-   Mencionar aspectos culturais como o "trompo" e "la propina".
-   Incorporar termos locais como "chilango" (morador da CDMX).
```

---

## Checklist

-   [ ] Auditoria completa da estrutura de domínio (ccTLD, subdomínio, subdiretório) e sua adequação para cada mercado-alvo.
-   [ ] Validação rigorosa da implementação `hreflang` em todas as páginas multilíngues/multiregionais, incluindo links recíprocos e `x-default`.
-   [ ] Configuração precisa de geotargeting no Google Search Console para domínios gTLD, associando subdiretórios/subdomínios a países específicos.
-   [ ] Realização de Keyword Research específica para cada idioma e região, identificando termos locais, gírias e intenções de busca.
-   [ ] Conteúdo localizado (não apenas traduzido) que ressoa culturalmente e utiliza dados e referências específicas do mercado-alvo.
-   [ ] Otimização de meta titles e descriptions para cada idioma/região, considerando a SERP local e o CTR esperado.
-   [ ] Implementação de CDNs globais e hosting otimizado para a velocidade de carregamento nos mercados-alvo.
-   [ ] Desenvolvimento de uma estratégia de link building focada na aquisição de backlinks de domínios locais e relevantes para cada mercado.
-   [ ] Otimização de Schema Markup (LocalBusiness, Product, Review) com dados específicos de cada localidade e idioma.
-   [ ] Monitoramento contínuo de desempenho (tráfego orgânico, rankings, conversões) por país/idioma no Google Analytics e GSC.
-   [ ] Implementação de navegação clara e seletor de idioma/região visível para o usuário.
-   [ ] Verificação de compatibilidade mobile e usabilidade em diferentes dispositivos e regiões.

---

## Métricas de Referência

| Métrica                      | Benchmark (Indústria) | Meta (Exemplo) |
|------------------------------|-----------------------|----------------|
| Tráfego Orgânico por Região  | +15% anualmente       | +20% (Alemanha) |
| Taxa de Conversão Local      | 1.5% - 3.0%           | 2.5% (França)   |
| Posição Média de Keyword Local | Top 5 para 20% das KWs | Top 5 para 25% |
| % de Sessões de Mercado Alvo | > 70%                 | 85%            |
| Páginas Indexadas por Idioma | > 90% das URLs Canônicas | 98%            |
| Custo por Aquisição (CPA) Local | R$ 50 - R$ 150        | R$ 70 (Brasil)  |

---

## Erros Comuns

1.  **Tradução Literal em vez de Localização**: Um site de e-commerce traduz "black friday deals" como "negócios de sexta-feira preta" para o Brasil, onde o termo correto e de maior busca é "promoções de Black Friday" ou "ofertas de Black Friday".
    *   **Como evitar**: Contratar tradutores nativos com expertise em marketing digital e SEO. Realizar pesquisa de termos e intenção de busca para cada mercado, garantindo que a linguagem utilizada ressoe com o público local e suas expressões idiomáticas. Exemplo: Para um produto de beleza, o termo "skin care" pode ser traduzido como "c