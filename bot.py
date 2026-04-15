import discord
from discord.ext import commands
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Keep-alive server عشان Railway ما يوقف البوت
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")
    def log_message(self, format, *args):
        pass  # يخفي logs الـ HTTP عشان ما تزحم

def run_server():
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# إعداد البوت
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"البوت شغال: {bot.user}")

@bot.command()
async def rules(ctx):
    await ctx.message.delete()

    embed1 = discord.Embed(title="📋 الشروط والأحكام", color=0x5865F2)
    embed1.add_field(name="", value=(
        "**لايمكن طلب استرجاع المبلغ بعد الشراء**\n"
        "**قلة احترامك لسبب التعويض أم شراء منتج سوف يتم طردك من السيرفر بدون أي تعويض أو أي استلام**\n"
        "**تستغرق جميع الطلبات من 5 دقائق الى 24 ساعة كحد أقصى**\n"
        "**يجب الدفع قبل استلام المنتج**\n"
        "**عند شراء نيترو يرجى تصوير مقطع فيديو أثناء الاستخدام لضمان حقوقك**\n"
        "**المتجر غير مسؤول عن أي استخدام مخالف للمنتج بعد تسليمه**\n"
        "**لايوجد ضمان على بعض المنتجات**\n"
        "**التقييم إلزامي للضمان — في حال عدم التقييم لايشملك ضمان**\n"
        "**يمنع كثرة المنشن في التكت — في حال كثرة المنشن سيتم إغلاق التذكرة فوراً**\n"
        "**الاشتراكات يمكنك إدخال حساب شخصين كحد أقصى**\n"
        "**أنا أبيع جميع منتجات المتجر لباب الرزق — في حال أسأت الاستخدام أنا غير مسؤول**"
    ), inline=False)

    embed2 = discord.Embed(title="📜 تفاصيل الضمان", color=0x5865F2)
    embed2.add_field(name="", value=(
        "**1.** بعض المنتجات تشمل ضمانًا محددًا ويتم توضيح تفاصيله قبل الشراء.\n"
        "**2.** بعد إتمام عملية الدفع لا يمكن استرجاع المبلغ نهائيًا.\n"
        "**3.** الضمان يشمل إصلاح المشكلة أو تعويض المنتج فقط.\n"
        "**4.** يتحمل العميل مسؤولية قراءة تفاصيل المنتج قبل الدفع.\n"
        "**5.** المتجر غير مسؤول عن سوء الاستخدام.\n"
        "**6.** في حال ثبوت مشكلة من طرف المتجر يتم التعامل معها ضمن شروط الضمان.\n"
        "**7.** إتمام عملية الشراء يعني موافقة العميل على جميع الشروط."
    ), inline=False)

    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    await ctx.send("||@everyone||")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
