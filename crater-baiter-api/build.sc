import mill._
import $ivy.`com.lihaoyi::mill-contrib-playlib:`,  mill.playlib._

object craterbaiterapi extends RootModule with PlayModule {

  def scalaVersion = "2.13.16"
  def playVersion = "3.0.8"
  def twirlVersion = "2.0.9"

  object test extends PlayTests
}
